from django.shortcuts import render, redirect
from .models import  User, Usuario,RolUsuario1
from django.contrib.auth import logout, authenticate, login
from app.forms import *
from django.db.models import Q
from django.views.generic import DetailView, ListView, CreateView, UpdateView, DeleteView
#rest frame work
from rest_framework import viewsets
import json
from django.conf import settings
import urllib.request

# Create your views here.

def inicio(request):
    return render(request,'index.html')

def inicio_sesion(request):
    return render(request,'login.html')

def registered(request):
    if request.method == 'POST':
        form = RegisterForm(request.POST)
    return render(request,'registered.html')

def user_register(request):
    if request.user.is_authenticated:
        response = redirect('/login/')
        return response
    # if this is a POST request we need to process the form data
    template = 'register.html'
   
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = RegisterForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            if User.objects.filter(username=form.cleaned_data['username']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Username already exists.'
                })
            elif User.objects.filter(email=form.cleaned_data['email']).exists():
                return render(request, template, {
                    'form': form,
                    'error_message': 'Email already exists.'
                })
            elif form.cleaned_data['password1'] != form.cleaned_data['password2']:
                return render(request, template, {
                    'form': form,
                    'error_message': 'Passwords do not match.'
                })
            else:
                # Create the user:
                user = User.objects.create_user(
                    form.cleaned_data['username'],
                    form.cleaned_data['email'],
                    form.cleaned_data['password1']
                )
                user.first_name = form.cleaned_data['firstname']
                user.last_name = form.cleaned_data['lastname']
                user.save()

                Query = RolUsuario1.objects.all().filter(DescipcionRol = 'Cliente')
                usuario = Usuario(
                    user=user,
                    DireccionUsuario = form.cleaned_data['DireccionUsuario'],
                    FechaRegistroUsuario = timezone.now(),
                    IdRol = Query[0]
                )
                usuario.save()

                # Login the user
                login(request, user)
               
                # redirect to accounts page:
                return redirect('/')

   # No post data availabe, let's just show the page.
    else:
        form = RegisterForm()

    return render(request, template, {'form': form})

