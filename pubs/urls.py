from django.conf.urls import url
from pubs import views
from pubs.views import PubsView, PubView

urlpatterns = [
    url(r'^$', PubsView.as_view(), name='pubs'),
    url(r'^home$', views.index, name='index'),
    url(r'^(?P<pub_id>[0-9]+)/$', PubView.as_view(), name='pub'),
    url(r'^nearme$', views.nearme, name='nearme'),
    url(r'^area$', views.area, name='area'),
    url(r'^area/(?P<local_authority>\w+( \w+)*)/$', views.local_pubs, name='local_pubs'),
    url(r'^change$',views.change, name='new'),
    url(r'^(?P<pub_id>[0-9]+)/change$', views.bound_form, name='change')
]
