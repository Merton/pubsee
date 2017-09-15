# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from pubs.models import Pub,Local_Authority

# Register your models here.
class PubAdmin(admin.ModelAdmin):
    list_display = ('name', 'address', 'postcode', 'local_authority')

admin.site.register(Pub, PubAdmin)
admin.site.register(Local_Authority)
