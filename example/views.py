from django.shortcuts import render
from .forms import SubscriberForm
from django.http import HttpResponse, HttpResponseRedirect
from products.models import *

def index(request):
    form=SubscriberForm(request.POST or None)
    if request.method =="POST" and form.is_valid():
        print (request.POST)
        form =form.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
    return render(request, "landing/index.html", locals())


def home(request):
    products_images=ProductImage.objects.filter(is_main=True, product__is_active=True)
    products_images_phones = products_images.filter(product__category__id=1)
    products_images_laptops = products_images.filter(product__category__id=2)
    return render(request, "landing/home.html", locals())

def about(request):

    return render(request, "landing/about.html", locals())

def delivery(request):
   
    return render(request, "landing/delivery.html", locals())