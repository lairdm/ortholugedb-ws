from django.conf.urls import patterns, url

from webui import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^json/genomedistance/(?P<mversion>\d+)/(?P<gpid1>\d+)/(?P<gpid2>\d+)/$', views.genomedistance, name="genomedistance"),
)
