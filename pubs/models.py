# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.

class Pub(models.Model):
    pub_id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=200)
    address = models.TextField()
    postcode = models.CharField(max_length=8)
    easting = models.IntegerField()
    northing = models.IntegerField()
    latitude = models.DecimalField(decimal_places=6,max_digits=8)
    longitude = models.DecimalField(decimal_places=6,max_digits=8)
    local_authority = models.TextField()


    def __str__(self):
        return self.name
