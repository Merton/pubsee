from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all$', views.publist, name='publist'),
    url(r'^(?P<pub_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^nearme$', views.nearme, name='nearme'),
    url(r'^area$', views.area, name='area'),
    url(r'^area/(?P<local_authority>\w+( \w+)*)/$', views.local_pubs, name='local_pubs'),
    url(r'^change$',views.change, name='new'),
    url(r'^change/(?P<pub_id>[0-9]+)/$', views.bound_form, name='change')
]
