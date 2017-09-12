# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from pubs.models import Pub
from pubs.scripts.pub_extensions import *

def index(request):
    return render(request, 'pubs/index.html')

def publist(request):
    publist = all_pubs
    context = {'publist': publist}
    return render(request, 'pubs/publist.html', context)

def detail(request, pub_id):
    pub = get_object_or_404(Pub, pub_id=pub_id)
    return render(request, 'pubs/detail.html', {'pub': pub})

def nearme(request):
    # near_pubs = pub_within(lat,long,5)
    return render(request, 'pubs/nearme.html')#, {'near_pubs': near_pubs})
