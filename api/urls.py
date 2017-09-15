from django.conf.urls import url

from .views import PubsView

urlpatterns = [
    url(r'^pubs', PubsView.as_view(), name="pubs")
]
