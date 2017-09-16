from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from ..models import Collection, Song

def index(request):
    cols = Collection.objects.all()
    return render(request, 'collections/index.html', {'collections': cols})

def show(request, id):
    collection = Collection.objects.get(id=id)
    return render(request, 'collections/show.html', {'collection': collection})

def add_song(request, id):
    collection = Collection.objects.get(id=id)
    collection.song_set.create(title=request.POST['title'],
                               album=request.POST['album'],
                               artist=request.POST['artist'],
                               composer=request.POST['composer'],
                               duration=request.POST['duration'])
    return redirect('show_collection', id=id)
    
@login_required
def new(request):
    return render(request, 'collections/new.html', {})

@login_required
def create(request):
    collection = Collection(name=request.POST['name'], user=request.user)
    collection.save()
    return redirect('index')