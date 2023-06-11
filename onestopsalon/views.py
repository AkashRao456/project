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

def contact(request):
    if request.method == "POST":
        return render(request, "onestopsalon/contact.html", {
        'message': "Thank you for contacting us. We will get in touch with you shortly"
        })
    else :
        return render(request, "onestopsalon/contact.html")
    





