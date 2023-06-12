from django.urls import path

from . import views
 
app_name = "onestopsalon"
urlpatterns =[
    path("", views.home, name="home"),
    path("salons", views.salons, name="salons"),
    path("contact", views.contact, name="contact"),
    path("feedback", views.feedback, name="feedback")
]

