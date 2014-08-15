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

class Analysis(models.Model):
    analysis_id = models.IntegerField(primary_key=True)
    analysis_type = models.CharField(max_length=9L)
    ing1_gp_id = models.IntegerField()
    ing1_version = models.IntegerField()
    ing2_gp_id = models.IntegerField()
    ing2_version = models.IntegerField()
    outg_gp_id = models.IntegerField()
    outg_version = models.IntegerField()
    microbedb_version = models.IntegerField()
    ortholuge_version = models.IntegerField()
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
    analysis_id = models.IntegerField()
    cluster_id = models.IntegerField()
    ing1_gene_id = models.IntegerField()
    ing2_gene_id = models.IntegerField()
    outg_gene_id = models.IntegerField(null=True, blank=True)
    inparalog = models.IntegerField(null=True, blank=True)
    dist1 = models.FloatField(null=True, blank=True)
    dist2 = models.FloatField(null=True, blank=True)
    dist3 = models.FloatField(null=True, blank=True)
    ratio1 = models.FloatField(null=True, blank=True)
    ratio2 = models.FloatField(null=True, blank=True)
    ratio3 = models.FloatField(null=True, blank=True)
    locfdr1 = models.FloatField(null=True, blank=True)
    locfdr2 = models.FloatField(null=True, blank=True)
    class_field = models.CharField(max_length=14L, db_column='class', blank=True) # Field renamed because it was a Python reserved word.
    inparalog1 = models.IntegerField(null=True, blank=True)
    inparalog2 = models.IntegerField(null=True, blank=True)
    ogroup1 = models.IntegerField(null=True, blank=True)
    ogroup2 = models.IntegerField(null=True, blank=True)
    ogroup3 = models.IntegerField(null=True, blank=True)
    ogroup4 = models.IntegerField(null=True, blank=True)
    ogroup5 = models.IntegerField(null=True, blank=True)
    ing1_gp_id = models.IntegerField(null=True, blank=True)
    ing2_gp_id = models.IntegerField(null=True, blank=True)
    cluster_count1 = models.IntegerField(null=True, blank=True)
    cluster_count2 = models.IntegerField(null=True, blank=True)
    new_class = models.CharField(max_length=14L, blank=True)
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
    status = models.IntegerField()
    class Meta:
        db_table = 'run_status'

class Updatelog(models.Model):
    orthodb_version = models.IntegerField(primary_key=True)
    microbedb_version = models.IntegerField()
    update_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        db_table = 'updatelog'

