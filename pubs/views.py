# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from pubs.models import Pub

def index(request):
    pub_list = Pub.objects.all()
    context = {'pub_list': pub_list}
    return render(request, 'pubs/index.html', context)

def detail(request, pub_id):
    pub = get_object_or_404(Pub, pub_id=pub_id)
    return render(request, 'pubs/detail.html', {'pub': pub})
