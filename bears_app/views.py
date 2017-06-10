from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Collection, Song

def index(request):
    cols = Collection.objects.all()
    return render(request, 'collections/index.html', {'collections': cols})

def new_collection(request):
    return render(request, 'collections/new.html', {})

def create_collection(request):
    collection = Collection(name=request.POST['name'], user=request.user)
    collection.save()
    return redirect('index')