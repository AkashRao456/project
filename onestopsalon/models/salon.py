from django.db import models
from .category import Category

class Salon(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=50)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to="onestopsalon/",max_length=250,null=True,default=None)
    phone = models.IntegerField(default=0)

    @staticmethod
    def get_all_salons():
        return Salon.objects.all()