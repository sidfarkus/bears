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
    #new_user = User.objects.create_user('john', 'lennon@thebeatles.com', 'johnpassword')
    collection = Collection(name=request.POST['name'], user=new_user)
    collection.save()
    return redirect('index')