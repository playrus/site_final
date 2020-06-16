from django.conf.urls import url
from . import views

urlpatterns = [
     url(r'^$', views.home, name='home'),
     url(r'land/', views.index, name = 'index'),
     url(r'about/', views.about),
     url(r'delivery/', views.delivery),
]