from django.shortcuts import render
from .forms import SubscriberForm
from django.http import HttpResponse, HttpResponseRedirect
from products.models import *


def home(request):
    products_images=ProductImage.objects.filter(is_main=True, product__is_active=True)
    products_images_cat1 = products_images.filter(product__category__id=1)
    products_images_cat2 = products_images.filter(product__category__id=2)
    products_images_discount = products_images.filter(product__is_discount=True)
    return render(request, "landing/home.html", locals())

def about(request):

    return render(request, "landing/about.html", locals())

def delivery(request):
   
    return render(request, "landing/delivery.html", locals())