from django.shortcuts import render, redirect
from email import message
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from mysite import settings
from django.views.generic import ListView, DetailView
#from .models import Post

# Create your views here.

def home(request): 
    return render(request, 'main.html')

def gallery(request):
    return render(request, 'gallery.html')