from django.contrib.auth.models import User
from django.db import models

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=20)
    def __str__(self):
        return self.user.username


class Brand(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name

class Motorbike(models.Model):
    name = models.CharField(max_length=255)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)
    price = models.IntegerField()
    image = models.ImageField(null=True, blank=True)
    engine_type = models.CharField(max_length=255)
    displacement = models.DecimalField(max_digits=6, decimal_places=2)
    piston = models.CharField(max_length=255)
    compression_ratio = models.DecimalField(max_digits=4, decimal_places=2)
    lubrication = models.CharField(max_length=255)
    ignition = models.CharField(max_length=255)
    gearbox = models.CharField(max_length=255)
    max_power = models.CharField(max_length=255)
    max_torque = models.CharField(max_length=255)
    dimensions = models.CharField(max_length=255)
    seat_height = models.DecimalField(max_digits=6, decimal_places=2)
    fuel_capacity = models.DecimalField(max_digits=6, decimal_places=2)
    def __str__(self):
        return self.name


class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    motorbike = models.ForeignKey(Motorbike, on_delete=models.CASCADE)
    order_date = models.DateField()
    def __str__(self):
        return self.ID

    
