from django.contrib import admin
from .models.salon import Salon
from .models.category import Category

class AdminSalon(admin.ModelAdmin):
    list_display = ['name', 'address', 'phone', 'image', 'category']

class AdminCategory(admin.ModelAdmin):
    list_display = ['name']

# Register your models here.
admin.site.register(Salon, AdminSalon)
admin.site.register(Category, AdminCategory)
