from rest_framework import serializers
from pubs import models

class PubsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Pub
        fields = '__all__'
