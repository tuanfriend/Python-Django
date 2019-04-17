#This is view from perosnal blog app
from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages

def blog(request):
    return render(request, "PersonalBlog/blog.html")