from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

#from .models import

# Create your views here.

def index(request):
    return render(request, "first_page/index.html")

def games_page(request):
    return render(request, "first_page/games_page.html")
