from django.urls import path, include
from .views import car


urlpatterns = [
    path("car/", car, name="car" ),
]