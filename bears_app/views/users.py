from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages

def new(request):
   form = UserCreationForm()
   return render(request, 'registration/sign_up.html', {'form': form})

def create(request):
    username, password, confirm = request.POST['username'], request.POST['password1'], request.POST['password2']
    if password != confirm:
      messages.error(request, 'Your passwords did not match loser 😠')
      return redirect('new_user')
    else:
      User.objects.create_user(username=username,
                               last_name='cool',
                               email='aero@secretlair.com',
                               password=password,
                               first_name='aero')
      messages.info(request, 'Thanks for signing up!')
      return redirect('login')