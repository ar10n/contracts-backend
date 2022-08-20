from django.contrib.auth.models import User
from django.db import models


class Client(models.Model):
    name = models.CharField(max_length=64, unique=True)
    inn = models.CharField(max_length=10, unique=True)
    phone = models.CharField(max_length=10, blank=True)
    email = models.CharField(max_length=64, blank=True)
    comment = models.TextField(blank=True)

    def __str__(self):
        return self.name


class Company(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Manufacturer(models.Model):
    name = models.CharField(max_length=128, unique=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=64)
    manufacturer = models.ForeignKey(
        Manufacturer, on_delete=models.CASCADE, related_name="products"
    )

    def __str__(self):
        return self.name


class Region(models.Model):
    name = models.CharField(max_length=64, unique=True)

    def __str__(self):
        return self.name


class Contract(models.Model):
    number = models.CharField(max_length=64)
    notice_number = models.CharField(max_length=32, blank=True)
    start_date = models.DateField()
    end_date = models.DateField(blank=True, null=True)
    price = models.DecimalField(max_digits=24, decimal_places=2)
    days_to_deliver = models.IntegerField(default=1)
    days_to_pay = models.IntegerField(default=7)
    client = models.ForeignKey(Client, on_delete=models.CASCADE, related_name="modules")
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, related_name="modules"
    )
    region = models.ForeignKey(Region, on_delete=models.CASCADE, related_name="modules")
    is_done = models.BooleanField(default=False)
    products = models.ManyToManyField(Product)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.number


class Claim(models.Model):
    name = models.CharField(max_length=128)
    start_date = models.DateField()
    deadline = models.DateField(blank=True, null=True)
    comment = models.TextField(blank=True)
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="claims"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Shipment(models.Model):
    number = models.CharField(max_length=32)
    price = models.DecimalField(decimal_places=2, max_digits=16)
    start_date = models.DateField()
    delivery_date = models.DateField()
    pay_date = models.DateField()
    is_delivered = models.BooleanField(default=False)
    is_paid = models.BooleanField(default=False)
    contract = models.ForeignKey(
        Contract, on_delete=models.CASCADE, related_name="shipments"
    )
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.number
