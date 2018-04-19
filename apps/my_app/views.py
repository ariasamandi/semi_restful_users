# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from models import *

# Create your views here.
def index(request):
    context = {
        "User": User.objects.all()
    }
    return render(request, 'my_app/index.html', context)
def new(request):
    return render(request, 'my_app/new.html')
def edit(request, number):
    context = {
        "User": User.objects.get(id=number)
    }
    return render(request, 'my_app/edit.html', context)
def show(request, number):
    context = {
        "User": User.objects.get(id=number)
    }
    return render(request, 'my_app/show.html', context)
def create(request):
    User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email']) 
    return redirect('/')
def destroy(request, number):
    User.objects.get(id=number).delete()
    return redirect('/')
def update(request, number):
    b = User.objects.get(id=number)
    b.first_name = request.POST['first_name']
    b.last_name = request.POST['last_name']
    b.email = request.POST['email']
    b.save()
    return redirect('/')
# def new_process(request):
#     request.session['first_name'] = request.POST['first_name']
#     request.session['last_name'] = request.POST['last_name']
#     request.session['email'] = request.POST['email']
#     return redirect('/')