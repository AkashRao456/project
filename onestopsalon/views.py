from django.shortcuts import render
from django.http import HttpResponse
from .models.salon import Salon


# Create your views here.

def salons(request):
    salons = Salon.get_all_salons();
    print(salons)
    return render(request, "onestopsalon/salons.html", {'salons': salons})

def home(request):
    return render(request, "onestopsalon/homepage.html")





