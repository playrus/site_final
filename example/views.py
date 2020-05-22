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
    products_images=ProductImage.objects.filter(is_main=True)
    return render(request, "landing/home.html", locals())