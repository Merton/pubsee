# from pubs.models import Pub
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from .serializers import PubsSerializer
from pubs.models import Pub, Local_Authority
# Create your views here.
class PubsView(ListCreateAPIView):
    serializer_class = PubsSerializer
    queryset = Pub.objects.all()
