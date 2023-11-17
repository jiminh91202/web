from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.

class Customer(models.Model):
    phone_number = models.CharField(max_length=15)

class Brand(models.Model):
    name = models.CharField(max_length=255)
    ID = models.AutoField(primary_key=True)

class Motorbike(models.Model):
    ID = models.AutoField(primary_key=True)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=14, decimal_places=2)

class Order(models.Model):
    ID = models.AutoField(primary_key=True)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    motorbike = models.ForeignKey(Motorbike, on_delete=models.CASCADE)
    order_date = models.DateField()


    
