from django.contrib import admin
from .models import Manufacturers, Products, Customers, Orders, OrderDetails, Employees, CustomerReviews

admin.site.register(Manufacturers)
admin.site.register(Products)
admin.site.register(Customers)
admin.site.register(Orders)
admin.site.register(OrderDetails)
admin.site.register(Employees)
admin.site.register(CustomerReviews)

class EmployessAdmin(admin.ModelAdmin):
    pass