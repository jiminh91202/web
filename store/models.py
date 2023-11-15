# Create your models here.
from django.db import models

class Manufacturer(models.Model):
    ManufacturerID = models.AutoField(primary_key=True)
    ManufacturerName = models.CharField(max_length=255)
    ContactInfo = models.TextField()
    class Meta:
        verbose_name_plural = 'manufacturers'
    
    

class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    QuantityInStock = models.IntegerField()
    Image = models.ImageField(upload_to='images/')
    Specifications = models.TextField()
    ManufacturerID = models.ForeignKey(Manufacturer, on_delete=models.CASCADE)
    YearManufactured = models.DateField()
    class Meta:
        verbose_name_plural = 'product'