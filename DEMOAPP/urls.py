from django.contrib import admin
from django.urls import path
from DEMOAPP import views

urlpatterns = [
    path('', views.Table, name ="table")
]


