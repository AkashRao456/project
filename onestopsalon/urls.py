from django.urls import path

from . import views
 
app_name = "onestopsalon"
urlpatterns =[
    path("", views.home, name="home"),
    path("salons", views.salons, name="salons")
]

