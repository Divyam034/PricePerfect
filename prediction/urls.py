from django.urls import path, include
from .views import carpage, predict


urlpatterns = [
    path("carpage/", carpage, name="carpage" ),
    path("carpage/predict", predict,name="predict"),
]