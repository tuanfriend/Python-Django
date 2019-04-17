#This is view from Login App
from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages

def index(request):
    return render(request, "FinalLog/login.html")

def signup(request):
    return render(request, "FinalLog/signup.html")

def regacc(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/signup')
    else:
        f_name = request.POST["firstname"]
        l_name = request.POST["lastname"]
        e_mail = request.POST["reg-email"]
        passw = bcrypt.hashpw(request.POST["reg-pw"].encode(), bcrypt.gensalt())
        User.objects.create(fname=f_name,lname=l_name,email=e_mail,pword=passw)
        user = User.objects.get(email = request.POST['reg-email'])
        request.session['user_id'] = user.id
        request.session['logged'] = True
        messages.success(request, "Successfully Registered!")
        return redirect("/blog")

def logacc(request):
    errors = User.objects.login_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
    else:
        request.session['logged'] = True
        user = User.objects.get(email = request.POST['log-email'])
        request.session['user_id'] = user.id
        # messages.success(request, 'Successfully loging in...!')
        return redirect('/blog')

def logout(request):
    request.session.clear()
    messages.success(request, 'Successfully logout!')
    return redirect('/')

def dashboard(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        user = User.objects.get(id=request.session['user_id'])
        content = {
            "user": user,
        }
        return render(request, "FinalLog/dashboard.html", content)
