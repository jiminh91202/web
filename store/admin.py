from django.contrib import admin

# Register your models here.
from .models import Manufacturer,Products

@admin.register(Manufacturer)
class ManufacturerAdmin(admin.ModelAdmin):
    list_display = ['ManufacturerID','ManufacturerName','ContactInfo']

@admin.register(Products)
class ProductsAdmin(admin.ModelAdmin):
    list_display = ['ProductID','ProductName','Description']
    
