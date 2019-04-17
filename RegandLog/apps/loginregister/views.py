from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, "loginregister/index.html")

def regacc(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            messages.error(request, value)
        # redirect the user back to the form to fix the errors
        return redirect('/')
    else:
        f_name = request.POST["firstname"]
        l_name = request.POST["lastname"]
        e_mail = request.POST["email"]
        if(request.POST["pw"]==request.POST["cpw"]):
            passw = bcrypt.hashpw(request.POST["pw"].encode(), bcrypt.gensalt())
            User.objects.create(fname=f_name,lname=l_name,email=e_mail,pword=passw)
        else:
            print("password not match")
        return redirect("/success")

def logacc(request):
    request.session['wrongemail']=''
    request.session['wrongpass']=''
    find_user = User.objects.filter(email=request.POST["email"])
    if len(find_user) == 0:
        request.session['wrongemail'] = "Wrong email please enter carefuly!!!"
        return redirect("/")
    else:
        user = User.objects.get(email=request.POST["email"])
        request.session['fname'] = user.fname
        request.session['lname'] = user.lname
        if bcrypt.checkpw(request.POST['pw'].encode(), user.pword.encode()):
            return redirect("/success")
        else:
            request.session['wrongpass'] = "Wrong password please enter again!"
            return redirect("/")

def successpg(request):
    content = {
        "fname": request.session['fname'],
        "lname": request.session['lname']
    }
    return render(request, "loginregister/success.html", content)

def logout(request):
    request.session.clear()
    return redirect('/')