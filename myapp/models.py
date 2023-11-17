from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.
class Brand(models.Model):
    name = models.CharField(max_length=255)
    ID = models.AutoField(primary_key=True, default=1)
    def __str__(self):
        return self.name
    
class Motorbike(models.Model):
    ID = models.AutoField(primary_key=True, default=1)
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=14, decimal_places=2)
    def __str__(self):
        return self.name

class Customer(models.Model):
    phone_number = models.CharField(max_length=15)

class Order(models.Model):
    ID = models.AutoField(primary_key=True, default=1)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    motorbike = models.ForeignKey(Motorbike, on_delete=models.CASCADE)
    order_date = models.DateField()
    def __str__(self):
        return f"Order {self.id}: {self.motorbike.name} for {self.customer.name} on {self.order_date}"

    
