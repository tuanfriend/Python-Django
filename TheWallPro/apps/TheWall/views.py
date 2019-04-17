from django.shortcuts import render, redirect
from .models import *
import bcrypt
from django.contrib import messages


def index(request):
    return render(request, "TheWall/login.html")

def signup(request):
    return render(request, "TheWall/signup.html")

def regacc(request):
    errors = User.objects.basic_validator(request.POST)
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/')
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
        return redirect("/dashboard")

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
        return redirect('/dashboard')

def successpg(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        user = User.objects.get(id=request.session['user_id'])
        content = {
            "user": user,
        }
        return render(request, "TheWall/success.html", content)

def logout(request):
    request.session.clear()
    messages.success(request, 'Successfully logout!')
    return redirect('/')

def dashboard(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        user = User.objects.get(id=request.session['user_id'])
        # for post in Message.objects.all():
        #     allcm += Comment.objects.filter(message=post.id).order_by('-created_at')[:4]
        content = {
            "user": user,
            "allmess": Message.objects.all().order_by('-created_at')[:8],
            # "allcm": Message.cmmess.all().order_by('-created_at')[:5]
            # Comment.objects.all()
        }
        return render(request, "TheWall/dashboard.html", content)

def postmess(request):
    user = User.objects.get(id=request.POST['userpost'])
    Message.objects.create(user=user, message=request.POST['post-mess'])
    return redirect('/dashboard')

def postcm(request):
    user = User.objects.get(id=request.POST['userpost'])
    postmess = Message.objects.get(id=request.POST['hidepost'])
    Comment.objects.create(message= postmess, user=user, comment=request.POST['post-cm'])
    return redirect('/dashboard')

def usermessage(request, id):
    user = User.objects.get(id=id)
    allmess = Message.objects.filter(user=user).order_by('-created_at')[:8]
    content = {
        "user": User.objects.get(id=request.session['user_id']),
        "allmess": allmess
    }
    return render(request, "TheWall/dashboard.html", content)

def editu(request):
    if request.session['logged'] == False:
        return redirect("/")
    elif request.session['logged'] == True:
        user = User.objects.get(id=request.session['user_id'])
        content = {
            "user": user
        }
    return render(request, "TheWall/edituser.html", content)

def btedit(request,id):
    print(request.POST)
    errors = User.objects.update_validator(request.POST)
    
    if len(errors) > 0:
        for key, value in errors.items():
            messages.error(request, value)
        return redirect('/edit')
    else:
        user = User.objects.get(id=id)
        user.fname = request.POST['up-fname']
        user.lname = request.POST["up-lname"]
        user.email = request.POST["up-email"]
        user.save()
        return redirect('/dashboard')


def delemessage(request,id):
    me = Message.objects.get(id=id)
    me.delete()
    return redirect('/dashboard')

# def postlike(request,messid):
#     new_like, created = Like.objects.get_or_create(user=request.session['user_id'], message=messid)
#     if not created:
#         number_of_likes = mess.like_set.all()
#     else:
#         mess = Message.objects.get(id=messid)
#         number_of_likes = mess.like_set.all().count()
#     content = {
#         "alllike": number_of_likes
#     }
#     return render(request, "TheWall/edituser.html", content)

def postlike(request,id):
    user = User.objects.get(id=request.session['user_id'])
    message = Message.objects.get(id=id)
    message.like.add(user)
    message.save()
    return redirect('/dashboard')