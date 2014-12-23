# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#     * Rearrange models' order
#     * Make sure each model has one field with primary_key=True
# Feel free to rename the models, but don't rename db_table values or field names.
#
# Also note: You'll have to insert the output of 'django-admin.py sqlcustom [appname]'
# into your database.
from __future__ import unicode_literals

from django.db import models
import pprint

RUN_STATUS = {'DIST_RUN': 1,
              'DIST_SUCCESS': 2,
              'RBB_RUN': 4,
              'RBB_SUCCESS': 8,
              'ORTHO_RUN': 16,
              'ORTHO_NO_OUTGP': 32,
              'ORTHO_SUCCESS': 64}

class Analysis(models.Model):
    analysis_id = models.AutoField(primary_key=True)
    analysis_type = models.CharField(max_length=9L)
    ing1_gp_id = models.IntegerField()
    ing1_version = models.IntegerField(default=0)
    ing2_gp_id = models.IntegerField()
    ing2_version = models.IntegerField(default=0)
    outg_gp_id = models.IntegerField(default=0)
    outg_version = models.IntegerField(default=0)
    microbedb_version = models.IntegerField()
    ortholuge_version = models.IntegerField(default=0)
    run_date = models.DateTimeField()
    ratio1_dist_img = models.TextField(blank=True)
    ratio2_dist_img = models.TextField(blank=True)
    ratio_stat_plot1_img = models.TextField(blank=True)
    ratio_stat_plot2_img = models.TextField(blank=True)
    preceded_by = models.IntegerField(null=True, blank=True)
    followed_by = models.IntegerField(null=True, blank=True)
    isvalid = models.IntegerField(null=True, blank=True)
    sgroup1 = models.IntegerField(null=True, blank=True)
    sgroup2 = models.IntegerField(null=True, blank=True)
    sgroup3 = models.IntegerField(null=True, blank=True)
    sgroup4 = models.IntegerField(null=True, blank=True)
    sgroup5 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'analysis'

class Gene(models.Model):
    gene_id = models.IntegerField(primary_key=True)
    gp_id = models.IntegerField()
    rpv_id = models.IntegerField()
    gid = models.IntegerField(null=True, blank=True)
    pid = models.IntegerField(null=True, blank=True)
    protein_accnum = models.CharField(max_length=12L, blank=True)
    start = models.IntegerField()
    end = models.IntegerField()
    strand = models.CharField(max_length=1L)
    gene_name = models.TextField(blank=True)
    locus_tag = models.TextField(blank=True)
    gene_product = models.TextField(blank=True)
    isvalid = models.IntegerField(null=True, blank=True)
    ogroup1 = models.IntegerField(null=True, blank=True)
    ogroup2 = models.IntegerField(null=True, blank=True)
    ogroup3 = models.IntegerField(null=True, blank=True)
    ogroup4 = models.IntegerField(null=True, blank=True)
    ogroup5 = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'gene'

class GenomeDistance(models.Model):
    gp_id1 = models.IntegerField()
    gp_id2 = models.IntegerField()
    distance = models.FloatField(default=0)
    microbedb_version = models.IntegerField()
    rbb_count = models.IntegerField(default=0)
    isvalid = models.IntegerField(null=True, default=1)
    update_date = models.DateField(auto_now_add=True)
    id = models.AutoField(primary_key=True, db_column='id')

    def to_struct(self, extra_objs = None):
        r = {field.name: field.value_to_string(self) for field in self._meta.fields}
        
        if extra_objs:
            r.update(extra_objs)   
        
        return r
    
    class Meta:
        managed = False
        db_table = 'genome_distance'

class GenomeName(models.Model):
    gp_id = models.IntegerField()
    taxon_id = models.IntegerField(null=True, blank=True)
    name = models.CharField(max_length=150L, blank=True)
    microbedb_version = models.IntegerField()
    isvalid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'genome_name'

class Groups(models.Model):
    group_id = models.IntegerField(primary_key=True)
    l1 = models.IntegerField(null=True, blank=True)
    l2 = models.IntegerField(null=True, blank=True)
    l3 = models.IntegerField(null=True, blank=True)
    l4 = models.IntegerField(null=True, blank=True)
    isvalid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'groups'

class GroupsBackup(models.Model):
    group_id = models.IntegerField(primary_key=True)
    l1 = models.IntegerField(null=True, blank=True)
    l2 = models.IntegerField(null=True, blank=True)
    l3 = models.IntegerField(null=True, blank=True)
    l4 = models.IntegerField(null=True, blank=True)
    isvalid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'groups_backup'

class GroupsOld(models.Model):
    group_id = models.IntegerField(primary_key=True)
    l1 = models.IntegerField(null=True, blank=True)
    l2 = models.IntegerField(null=True, blank=True)
    l3 = models.IntegerField(null=True, blank=True)
    l4 = models.IntegerField(null=True, blank=True)
    isvalid = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'groups_old'

class Ortholog(models.Model):
    ortholog_id = models.IntegerField(primary_key=True)
    analysis_id = models.ForeignKey(Analysis, db_column='analysis_id')
    cluster_id = models.IntegerField()
    ing1_gene_id = models.IntegerField()
    ing2_gene_id = models.IntegerField()
    outg_gene_id = models.IntegerField(default=0, blank=True)
    inparalog = models.IntegerField(default=0, blank=True)
    dist1 = models.FloatField(default=0)
    dist2 = models.FloatField(default=0)
    dist3 = models.FloatField(default=0)
    ratio1 = models.FloatField(default=0)
    ratio2 = models.FloatField(default=0)
    ratio3 = models.FloatField(default=0)
    locfdr1 = models.FloatField(default=0)
    locfdr2 = models.FloatField(default=0)
    class_field = models.CharField(max_length=14L, db_column='class', null=True) # Field renamed because it was a Python reserved word.
    inparalog1 = models.IntegerField(default=0)
    inparalog2 = models.IntegerField(default=0)
    ogroup1 = models.IntegerField(null=True, blank=True)
    ogroup2 = models.IntegerField(null=True, blank=True)
    ogroup3 = models.IntegerField(null=True, blank=True)
    ogroup4 = models.IntegerField(null=True, blank=True)
    ogroup5 = models.IntegerField(null=True, blank=True)
    ing1_gp_id = models.IntegerField(null=True, blank=True)
    ing2_gp_id = models.IntegerField(null=True, blank=True)
    cluster_count1 = models.IntegerField(null=True, blank=True)
    cluster_count2 = models.IntegerField(null=True, blank=True)
    new_class = models.CharField(max_length=14L, null=True)

    def to_struct(self, extra_objs = None):
        r = {field.name: field.value_to_string(self) for field in self._meta.fields}
        
        if extra_objs:
            r.update(extra_objs)   
        
        return r

    def to_tab(self):
        return "\t".join([('\\N' if not getattr(self, field.name) and field.null else field.value_to_string(self)) for field in self._meta.fields])
#        return "\t".join([('NULL' if not getattr(self, field.name) and field.null else field.value_to_string(self)) for field in self._meta.fields])
            
    @classmethod
    def get_fields(cls):
        return [f.get_attname_column()[1] for f in cls._meta.fields]
        
    @classmethod
    def updated_row(cls, analysis_id, cluster_id, ing1_gene_id, ing2_gene_id, update_fields = None):
        try:
            ortholog = Ortholog.objects.get(analysis_id=analysis_id, cluster_id=cluster_id, ing1_gene_id=ing1_gene_id, ing2_gene_id=ing2_gene_id)
        
            fields = {f.get_attname_column()[1]: f.name for f in ortholog._meta.fields}
            
            for field,value in update_fields.iteritems():
                print "{} {}".format(field, value)
                if field in fields.keys():
                    setattr(ortholog, fields[field], value)
                else:
                    print "Error, field {} not found, value {}".format(field, value)

            print "so far so good"
            return ortholog.to_tab()
            
        except Exception as e:
            print "Error: {}".format(str(e))
            pass
            

    class Meta:
        db_table = 'ortholog'

class OrtholugeStatus(models.Model):
    analysis_id = models.IntegerField()
    ortholuge = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'ortholuge_status'

class RbbStatus(models.Model):
    lower = models.IntegerField(null=True, blank=True)
    higher = models.IntegerField(null=True, blank=True)
    rbb = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'rbb_status'

class RbbStatusOld(models.Model):
    lower_higher = models.CharField(max_length=15L)
    lower = models.IntegerField(null=True, blank=True)
    higher = models.IntegerField(null=True, blank=True)
    rbb = models.IntegerField()
    last_updated = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'rbb_status_old'

class RunGenomeStatus(models.Model):
    gp_id = models.IntegerField(unique=True)
    status = models.IntegerField(null=True, blank=True)
    class Meta:
        db_table = 'run_genome_status'

class RunStatus(models.Model):
    gp_id1 = models.IntegerField()
    gp_id2 = models.IntegerField()
    status = models.IntegerField(default=0)
    
    @classmethod
    def update_status(cls, gpid1, gpid2, status_bit):
        try:
            obj, created = RunStatus.objects.get_or_create(gp_id1 = gpid1, gp_id2 = gpid2)
            
            if created:
                obj.status = status_bit
            else:
                obj.status = obj.status | status_bit
                
            obj.save()
        except Exception as e:
            pass

    @classmethod
    def remove_status(cls, gpid1, gpid2, status_bit):
        try:
            obj, created = RunStatus.objects.get_or_create(gp_id1 = gpid1, gp_id2 = gpid2)
            
            if not created:
                obj.status = obj.status & ~status_bit
                
            obj.save()
        except Exception as e:
            pass
    
    @classmethod
    def isset(cls, gpid1, gpid2, status_bit):
        try:
            obj = RunStatus.objects.get(gp_id1 = gpid1, gp_id2 = gpid2)

            return True if obj.status & status_bit else False 
        except Exception as e:
            print str(e)
            raise Exception("run pair not found")

    @classmethod
    def getstatus(cls, gpid1, gpid2):
        try:
            obj = RunStatus.objects.get(gp_id1 = gpid1, gp_id2 = gpid2)

            return obj.status
        except Exception as e:
            print str(e)
            raise Exception("run pair not found")
    
    class Meta:
        db_table = 'run_status'

class Updatelog(models.Model):
    orthodb_version = models.IntegerField(primary_key=True)
    microbedb_version = models.IntegerField()
    update_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'updatelog'

