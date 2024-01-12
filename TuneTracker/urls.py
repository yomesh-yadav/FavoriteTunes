from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home,name="home"),
    path('all_songs', views.all_songs,name="predict"),

   
]