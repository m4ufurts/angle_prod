from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import auth

def index(request):
    return render(request, 'dashboard.html')