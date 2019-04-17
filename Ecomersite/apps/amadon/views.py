from django.shortcuts import render, HttpResponse, redirect
from .models import *


def index(request):
    content = {
        "items": Product.objects.all()
    }
    return render(request, "amadon/index.html", content)

def process(request):
    item_id = request.POST["itemid"]
    request.session['quantity'] = request.POST["qty"]
    p_item = Product.objects.get(id=item_id)
    request.session['total'] = p_item.price*int(request.session['quantity'])

    return redirect("/checkout")

def checkout(request):
    content = {
        "quality" : request.session['quantity'],
        "total" : request.session['total']
    }
    return render(request, "amadon/checkout.html", content)
