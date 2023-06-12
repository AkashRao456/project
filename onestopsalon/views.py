from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models.salon import Salon
from django.conf import settings


# Create your views here.

def salons(request):
    salons = Salon.get_all_salons();
    print(salons)
    return render(request, "onestopsalon/salons.html", {'salons': salons})

def home(request):
    return render(request, "onestopsalon/homepage.html")


def feedback(request):
    if request.method == "POST":
        return render(request, "onestopsalon/feedback.html", {
        'message': "Thank you for your feedback. We will try to work on that."
        })
    else :
        return render(request, "onestopsalon/feedback.html")
    
def contact(request):
    return render(request, "onestopsalon/contact.html")




