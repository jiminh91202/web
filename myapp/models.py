from django.db import models
# Create your models here.

class Manufacturers(models.Model):
    ManufacturerID = models.AutoField(primary_key=True)
    ManufacturerName = models.CharField(max_length=255)
    ContactInfo = models.TextField()

class Products(models.Model):
    ProductID = models.AutoField(primary_key=True)
    ProductName = models.CharField(max_length=255)
    Description = models.TextField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)
    QuantityInStock = models.IntegerField()
    ImageURL = models.CharField(max_length=255)
    Specifications = models.TextField()
    ManufacturerID = models.ForeignKey(Manufacturers, on_delete=models.CASCADE)
    YearManufactured = models.DateField()

class Customers(models.Model):
    CustomerID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Email = models.CharField(max_length=255)
    PhoneNumber = models.CharField(max_length=255)
    ShippingAddress = models.TextField()

class Orders(models.Model):
    OrderID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    OrderDate = models.DateField()
    OrderStatus = models.CharField(max_length=255)
    ShippingInfo = models.TextField()

class OrderDetails(models.Model):
    OrderID = models.ForeignKey(Orders, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    Quantity = models.IntegerField()
    Price = models.DecimalField(max_digits=10, decimal_places=2)

class Employees(models.Model):
    EmployeeID = models.AutoField(primary_key=True)
    Name = models.CharField(max_length=255)
    Position = models.CharField(max_length=255)
    ContactInfo = models.TextField()

class CustomerReviews(models.Model):
    ReviewID = models.AutoField(primary_key=True)
    CustomerID = models.ForeignKey(Customers, on_delete=models.CASCADE)
    ProductID = models.ForeignKey(Products, on_delete=models.CASCADE)
    ReviewContent = models.TextField()
    Rating = models.IntegerField()
