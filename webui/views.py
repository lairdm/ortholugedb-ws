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

import json
import re
import pprint
import os
import base64

def index(request):
        return render(request, 'index.html')

@csrf_exempt
def genomedistance(request, mversion, gpid1, gpid2):
    context = {}

    context['status'] = "OK"

    try:
        dist, created = GenomeDistance.objects.get_or_create(gp_id1=gpid1, gp_id2=gpid2, microbedb_version=mversion)
            
    except Exception as e:
        return HttpResponse(status=400)
    
    if request.method == 'POST':
        try:
            json_data = json.loads(request.body)

            for k in json_data.keys():
                if k not in dist._meta.fields:
                    raise Exception("Error, invalid key")
                setattr(dist, k, json_data[k])

            dist.save()
        except Exception as e:
            context['status'] = "ERROR"
            context['errmsg'] = str(e)
        
    context['distance'] = dist.to_struct()
                
    data = json.dumps(context, indent=4, sort_keys=True, cls=DjangoJSONEncoder)

    return HttpResponse(data, content_type="application/json")

