from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, render_to_response
from django.template import RequestContext
from django.conf import settings
from webui.models import *
from django.core.urlresolvers import reverse
from django.core.serializers.json import DjangoJSONEncoder
from django.views.decorators.csrf import csrf_exempt
from django.db.models.fields import FieldDoesNotExist
from django.db import connection

import json
import re
import pprint
import os
import base64
import tempfile
import os

def index(request):
        return render(request, 'index.html')

@csrf_exempt
def fetchrunstatus(request, gpid1, gpid2):
    context = {}

    context['status'] = "OK"

    try:
        context['statusbits'] = RunStatus.getstatus(gpid1, gpid2)
        
    except Exception as e:
        context['status'] = "ERROR"
        context['errmsg'] = str(e)
    
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def testrunstatus(request, gpid1, gpid2, statusbit):
    context = {}

    context['status'] = "OK"

    try:
        context['isset'] = str(RunStatus.isset(gpid1, gpid2, long(statusbit)))
        
    except Exception as e:
        context['status'] = "ERROR"
        context['errmsg'] = str(e)
    
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def setrunstatus(request, gpid1, gpid2, statusbit):
    context = {}

    context['status'] = "OK"

    try:
        RunStatus.update_status(gpid1, gpid2, long(statusbit))
    except Exception as e:
        context['status'] = "ERROR"
        context['errmsg'] = str(e)
    
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def removerunstatus(request, gpid1, gpid2, statusbit):
    context = {}

    context['status'] = "OK"

    try:
        RunStatus.remove_status(gpid1, gpid2, long(statusbit))
    except Exception as e:
        context['status'] = "ERROR"
        context['errmsg'] = str(e)
    
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")
        

def getorthologs(request, aid):
    context = {}

    context['status'] = "OK"

    context['orthologs'] = []
    
    try:
        orthologs = Ortholog.objects.filter(analysis_id=aid)

        for o in orthologs:
            context['orthologs'].append(o.to_struct())
    except Exception as e:
            context['status'] = "ERROR"  
            context['errmsg'] = str(e)
                
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def genomedistance(request, mversion, gpid1, gpid2):
    context = {}

    context['status'] = "OK"

    if request.method == 'POST':

        try:
            if RunStatus.isset(gpid1, gpid2, RUN_STATUS['DIST_SUCCESS']):
                context['status'] = "DUPLICATE"

                data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

                return HttpResponse(data, content_type="application/json")

        except Exception as e:
            pass

        try:
            dist, created = GenomeDistance.objects.get_or_create(gp_id1=gpid1, gp_id2=gpid2, microbedb_version=mversion)            
        except Exception as e:
            return HttpResponse(status=400)
    
        try:
            json_data = json.loads(request.body)

            for k in json_data.keys():
                dist._meta.get_field(k)

                setattr(dist, k, json_data[k])

            dist.save()
            
            RunStatus.update_status(gpid1, gpid2, RUN_STATUS['DIST_RUN'] | RUN_STATUS['DIST_SUCCESS'])

            context['distance'] = dist.to_struct()

        except FieldDoesNotExist as e:
            context['status'] = "ERROR"
            context['errmsg'] = "Field does not exist: " + str(e)           
        except Exception as e:
            context['status'] = "ERROR"
            context['errmsg'] = str(e)


    else:
        try:
            dist = GenomeDistance.objects.get(gp_id1=gpid1, gp_id2=gpid2, microbedb_version=mversion)

            context['distance'] = dist.to_struct()
        except Exception as e:
            context['status'] = "ERROR"  
            context['errmsg'] = str(e)
                
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")


@csrf_exempt
def genomedistanceonly(request, gpid1, gpid2):
    context = {}

    context['status'] = "OK"

    try:
        dist = GenomeDistance.objects.filter(gp_id1=gpid1, gp_id2=gpid2).order_by('-microbedb_version')[0]

        context['distance'] = dist.to_struct()
    except Exception as e:
            context['status'] = "ERROR"  
            context['errmsg'] = str(e)
                
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")

@csrf_exempt
def outgroupcontenders(request, gpid1, gpid2, distance):
    context = {}
 
    context['status'] = "OK"

    context['contenders'] = []

    print "{} {} {}".format(gpid1, gpid2, distance)

    params = [distance, gpid1, gpid2, distance]

    try:
        for res in GenomeDistance.objects.raw("SELECT genome_distance.gp_id1, genome_distance.distance, genome_distance.rbb_count, genome_distance.id \
        FROM genome_distance \
        WHERE genome_distance.distance > %s AND genome_distance.gp_id2 = %s AND genome_distance.gp_id1 in \
            (SELECT other.gp_id1 \
            FROM genome_distance other \
            WHERE other.gp_id2 = %s AND other.distance > %s AND other.isvalid = 1) \
            ORDER BY genome_distance.distance", params):
            context['contenders'].append([res.gp_id1, res.distance, res.rbb_count])

        for res in GenomeDistance.objects.raw("SELECT genome_distance.gp_id1, genome_distance.distance, genome_distance.rbb_count, genome_distance.id \
        FROM genome_distance \
        WHERE genome_distance.distance > %s AND genome_distance.gp_id2 = %s AND genome_distance.gp_id1 in \
            (SELECT other.gp_id2 \
            FROM genome_distance other \
            WHERE other.gp_id1 = %s AND other.distance > %s AND other.isvalid = 1) \
            ORDER BY genome_distance.distance", params):
            context['contenders'].append([res.gp_id1, res.distance, res.rbb_count])

        for res in GenomeDistance.objects.raw("SELECT genome_distance.gp_id2, genome_distance.distance, genome_distance.rbb_count, genome_distance.id \
        FROM genome_distance \
        WHERE genome_distance.distance > %s AND genome_distance.gp_id1 = %s AND genome_distance.gp_id2 in \
            (SELECT other.gp_id2 \
            FROM genome_distance other \
            WHERE other.gp_id1 = %s AND other.distance > %s AND other.isvalid = 1) \
            ORDER BY genome_distance.distance", params):
            context['contenders'].append([res.gp_id2, res.distance, res.rbb_count])

        for res in GenomeDistance.objects.raw("SELECT genome_distance.gp_id2, genome_distance.distance, genome_distance.rbb_count, genome_distance.id \
        FROM genome_distance \
        WHERE genome_distance.distance > %s AND genome_distance.gp_id1 = %s AND genome_distance.gp_id2 in \
            (SELECT other.gp_id1 \
            FROM genome_distance other \
            WHERE other.gp_id2 = %s AND other.distance > %s AND other.isvalid = 1) \
            ORDER BY genome_distance.distance", params):
            context['contenders'].append([res.gp_id2, res.distance, res.rbb_count])
    
    except Exception as e:
            context['status'] = "ERROR"  
            context['errmsg'] = str(e)
            
    context['count'] = len(context['contenders'])
            
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")
    
@csrf_exempt
def putortholuge(request, analysis_id):
    context = {}
    
    context['status'] = "OK"

    if request.method == 'POST':

        try:
            analysis = Analysis.objects.get(analysis_id=analysis_id)
            
        except Exception as e:
            return HttpResponse(status=400)

        try:
            analysis = Analysis.objects.get(analysis_id = analysis_id)
            analysis.analysis_type = 'ortholuge'

#            print "{}".format(request.body)
            json_data = json.loads(request.body)
            #pprint.pprint(json_data)
            
            orthologs = json_data['orthologs']
            
            with tempfile.NamedTemporaryFile() as tf:
                field_str = ",".join(Ortholog.get_fields())

                for o in orthologs:
                    row = Ortholog.updated_row(analysis_id, o['cluster_id'], o['ing1_gene_id'], o['ing2_gene_id'], o['updates'])
                    
                    tf.write(row + "\n")
                    
                tf.flush()
                tfName = tf.name

                print "filename: {}".format(tfName)
                os.system("cp " + tfName + " /tmp/ortholuge/")

                params = [tfName]
                cursor = connection.cursor()
                query_str = "LOAD DATA LOCAL INFILE %s REPLACE INTO TABLE ortholog FIELDS TERMINATED BY '\t' ({})".format(field_str)
                print "{}".format(query_str)
                res = cursor.execute(query_str, params)
                pprint.pprint(res)

            analysis.save()

            RunStatus.update_status(analysis.ing1_gp_id, analysis.ing2_gp_id, RUN_STATUS['ORTHO_RUN'] | RUN_STATUS['ORTHO_SUCCESS'])

            
        except Exception as e:
            print str(e)
            context['errstr'] = str(e)
            context['status'] = "ERROR"
            pass

    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")
            

@csrf_exempt
def putrbb(request, mversion, gpid1, gpid2):
    context = {}
 
    context['status'] = "OK"

    if request.method == 'POST':

        try:
            if RunStatus.isset(gpid1, gpid2, RUN_STATUS['RBB_SUCCESS']):
                context['status'] = "DUPLICATE"

                data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

                return HttpResponse(data, content_type="application/json")
        except:
            pass

        
        try:
            json_data = json.loads(request.body)
            
            rbbs = json_data['rbbs']
            
            # Ensure we can write the data to a temp file before
            # we create an analysis entry
            with tempfile.NamedTemporaryFile() as tf:
                
                for rbb in rbbs:
                    tf.write("\\N\t{}\t{}\t{}\t{}\t{}\t{}\n".format(rbb['cluster_id'], rbb['ing1_gene_id'], rbb['ing2_gene_id'], rbb['inparalog'], rbb['inparalog1'], rbb['inparalog2']))

                tf.flush()
                tfName = tf.name

#                print "rbb_count: {}".format(json_data['rbb_count'])
                
#                print "filename: {}".format(tfName)
#                os.system("cp " + tfName + " /tmp/ortholuge/")

                # We have the orthologs written to a file, 
                # make the analysis!
                analysis = Analysis(analysis_type = 'rbb', microbedb_version = mversion, ing1_gp_id = gpid1, ing2_gp_id = gpid2, isvalid = 0)
                analysis.save()

                aid = analysis.analysis_id
                
                # Load the RBBs!
                params = [tfName, aid]
                cursor = connection.cursor()
                res = cursor.execute("LOAD DATA LOCAL INFILE %s IGNORE INTO TABLE ortholog FIELDS TERMINATED BY '\t' (@analysis_id, cluster_id, ing1_gene_id, ing2_gene_id, inparalog, inparalog1, inparalog2) SET analysis_id = %s", params)
#                pprint.pprint(res)

                dist, created = GenomeDistance.objects.get_or_create(gp_id1=gpid1, gp_id2=gpid2, microbedb_version=mversion)
                dist.rbb_count = json_data['rbb_count']
                dist.save()

                RunStatus.update_status(gpid1, gpid2, RUN_STATUS['RBB_RUN'] | RUN_STATUS['RBB_SUCCESS'])

                analysis.isvalid = 1
                analysis.save()
                
                context['analysis_id'] = aid

        except Exception as e:
#            print "Exception!"
#            print str(e)
            context['status'] = "ERROR"
            context['errmsg'] = str(e)
            
    
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")
