from django.contrib import admin
from django.urls import path, include
from django.urls import path
from . import views
from django.conf.urls import url



urlpatterns = [
    path('', views.index, name='index'),
    path('english', views.english, name='english'),
]
