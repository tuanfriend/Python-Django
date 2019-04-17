from django.shortcuts import render, HttpResponse, redirect
from .models import *
from django.contrib import messages

def index(request):
    return render(request, "TheShows/index.html")

def allshows(request):
    content = {
        "all_shows" : dbshows.objects.all()
    }
    return render(request, "TheShows/shows.html", content)

def addshows(request):
    return render(request, "TheShows/newshow.html")

def addshowsBt(request):
    errors = dbshows.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            print(messages.error(request, value))
        # redirect the user back to the form to fix the errors
        return redirect('/addshow')
    else:
        title = request.POST["title_input"]
        netwk = request.POST["network_input"]
        redate = request.POST["date_input"]
        desc = request.POST["des_input"]
        lastshow = dbshows.objects.last()
        dbshows.objects.create(title=title,network=netwk,releasedate=redate,descrip=desc)
        return redirect('/shows/'+ str(lastshow.id+1))

def showDT(request,id):
    content = {
        "detail": dbshows.objects.get(id=id)
    }
    return render(request, "TheShows/showdetail.html", content)

def showedit(request,id):
    content = {
        "detail": dbshows.objects.get(id=id)
    }
    return render(request, "TheShows/edit.html", content)

def updatebt(request):
    currentShow = dbshows.objects.get(id=request.POST["hideid"])
    errors = dbshows.objects.basic_validator(request.POST)
    # check if the errors dictionary has anything in it
    if len(errors) > 0:
        # if the errors dictionary contains anything, loop through each key-value pair and make a flash message
        for key, value in errors.items():
            print(messages.error(request, value))
        # redirect the user back to the form to fix the errors
        return redirect('/shows/'+ str(currentShow.id)+'/edit')
    else:
        currentShow.title = request.POST["title_input"]
        currentShow.network = request.POST["network_input"]
        currentShow.releasedate = request.POST["date_input"]
        currentShow.descrip = request.POST["des_input"]
        currentShow.save()
        return redirect('/shows/'+ str(currentShow.id))

def deleteBt(request,id):
    currentShow = dbshows.objects.get(id=id)
    currentShow.delete()
    return redirect('/shows')