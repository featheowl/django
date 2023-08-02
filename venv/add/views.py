from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    return HttpResponse("Привет, это главна страница")
def home(request):
    return HttpResponse("Дома, вид домашней страницы")

# Create your views here.
