from django import forms
from .models import *


class CheckoutContactForm(forms.Form):
    name = forms.CharField(required=True)
    phone = forms.CharField(required=True)
    email = forms.EmailField(required=True)
    sec_name = forms.CharField(required=True)
    comments = forms.CharField
    adress = forms.CharField(required=True)