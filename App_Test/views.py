from django.shortcuts import render, HttpResponse
import requests

# Create your views here.
from requests import Response


def login(request):
      return render(request,"login.html")

def news(request):
      return render(request,"news.html")

def sign_in(request):
      return render(request,"sign_in.html")
