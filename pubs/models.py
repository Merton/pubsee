# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models

# Create your models here.


class Pub(models.Model):
    fsa_id = models.IntegerField()
    name = models.CharField(max_length=200)
    address = models.TextField()
    postcode = models.CharField(max_length=8)
    easting = models.IntegerField()
    northing = models.IntegerField()
    latitude = models.DecimalField()
    longitude = models.DecimalField()
    local_authority = models.TextField()
