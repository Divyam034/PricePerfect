from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def car(request):
    return HttpResponse({"a":1})