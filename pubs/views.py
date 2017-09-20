# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render,get_object_or_404, get_list_or_404
from django.http import HttpResponse
from pubs.models import Pub, Local_Authority
from pubs.scripts.pub_extensions import *
from . forms import PubForm

# TODO: Change format to use view classes rather than just functions
def index(request):
    return render(request, 'pubs/index.html')

# Display the list of all pubs
def publist(request):
    publist = Pub.objects.all().order_by('local_authority')
    context = {'publist': publist}
    return render(request, 'pubs/publist.html', context)

# Display a map view of a single pub
def detail(request, pub_id):
    pub = get_object_or_404(Pub, pub_id=pub_id)
    return render(request, 'pubs/detail.html', {'pub': pub})

# display all pubs within a certain area
def nearme(request):
    near_pubs = pub_within(2)
    return render(request, 'pubs/nearme.html', {'near_pubs': near_pubs})

# TODO: Change output so it heads to /area/local_authority rather than just /area
# TODO: Change to GET not POST
def area(request):
    if request.method == 'POST': #Should be GET request
        local_authority = request.POST.get('area', None)
        return local_pubs(request, local_authority.title())

# All pubs in the local authority
def local_pubs(request, local_authority):
    local_pubs=get_list_or_404(Pub, local_authority__name=local_authority)
    return render(request, 'pubs/local_authority.html', {'local_pubs':local_pubs, 'local_authority':local_authority})

# Output a pub into a form for editing
def bound_form(request, pub_id):
    pub = get_object_or_404(Pub,pub_id=pub_id)
    form = PubForm(instance=pub)
    return render(request, 'pubs/pub.html', {'form': form})

# Create or modify a pub
def change(request):
    if request.method == 'POST':
        form = PubForm(request.POST)
        if form.is_valid():
            form.process()
            pub = form.save(commit=False)
            pub.save()
            return render(request, 'pubs/detail.html', {'pub': pub})
    else:
        form = PubForm()
    return render(request, 'pubs/pub.html', {'form': form})
