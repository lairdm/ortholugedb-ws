from django.conf.urls import patterns, url

from webui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^json/runstatus/(?P<gpid1>\d+)/(?P<gpid2>\d+)/$', views.fetchrunstatus, name="fetchrunstatus"),
    url(r'^json/testrunstatus/(?P<gpid1>\d+)/(?P<gpid2>\d+)/(?P<statusbit>\d+)/$', views.testrunstatus, name="testrunstatus"),
    url(r'^json/setrunstatus/(?P<gpid1>\d+)/(?P<gpid2>\d+)/(?P<statusbit>\d+)/$', views.setrunstatus, name="setrunstatus"),
    url(r'^json/removerunstatus/(?P<gpid1>\d+)/(?P<gpid2>\d+)/(?P<statusbit>\d+)/$', views.removerunstatus, name="removerunstatus"),
    url(r'^json/getorthologs/(?P<aid>\d+)/$', views.getorthologs, name="getorthologs"),
    url(r'^json/putrbb/(?P<mversion>\d+)/(?P<gpid1>\d+)/(?P<gpid2>\d+)/$', views.putrbb, name="putrbb"),
    url(r'^json/putortholuge/(?P<analysis_id>\d+)/$', views.putortholuge, name="putortholuge"),
    url(r'^json/genomedistance/(?P<gpid1>\d+)/(?P<gpid2>\d+)/$', views.genomedistanceonly, name="genomedistanceonly"),
    url(r'^json/genomedistance/(?P<mversion>\d+)/(?P<gpid1>\d+)/(?P<gpid2>\d+)/$', views.genomedistance, name="genomedistance"),
    url(r'^json/outgroupcontenders/(?P<gpid1>\d+)/(?P<gpid2>\d+)/(?P<distance>.+)/$', views.outgroupcontenders, name="outgroupcontenders"),
)
