from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'land/', views.index, name = 'index'),
     url('about/', views.about),
     url('delivery/', views.delivery),
]