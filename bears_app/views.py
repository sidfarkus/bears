from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from .models import Collection, Song
from django.contrib.auth.forms import UserCreationForm

def index(request):
    # User.objects.create_user(username='aero',
    #                          first_name='aero',
    #                          last_name='cool',
    #                          email='aero@secretlair.com',
    #                          password='aero')
    cols = Collection.objects.all()
    return render(request, 'collections/index.html', {'collections': cols})

def new_collection(request):
    return render(request, 'collections/new.html', {})

def create_collection(request):
    collection = Collection(name=request.POST['name'], user=request.user)
    collection.save()
    return redirect('index')

def new_user(request):
   form = UserCreationForm()
   return render(request, 'registration/sign_up.html', {'form': form})