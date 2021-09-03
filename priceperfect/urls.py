from django.contrib import admin
from django.urls import path, include
from priceperfect import views

urlpatterns = [

    path("", views.mainpage, name="mainpage")

]