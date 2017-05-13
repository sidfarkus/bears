from django.shortcuts import render
from django.http import HttpResponse
from .models import Collection, Song

def index(request):
    cols = Collection.objects.all()
    return render(request, 'collections/index.html', {'collections': cols})

def new_collection(request):
    return render(request, 'collections/new.html', {})