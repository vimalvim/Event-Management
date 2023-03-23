from django.db import models

class register1(models.Model):
    name =models.CharField(max_length=150)
    email =models.EmailField(max_length=150)
    phonenumber =models.CharField(max_length=12)
    gender =models.CharField(max_length=10)
    password =models.CharField(max_length=150)
    report =models.BooleanField(default=False,null=True)


class detail(models.Model):
    firstname =models.CharField(max_length=150)
    email =models.EmailField(max_length=150)
    phonenumber =models.CharField(max_length=12)
    address =models.CharField(max_length=12)
    city =models.CharField(max_length=12)
    country =models.CharField(max_length=12)
    Events =models.CharField(max_length=50, null=True)
    food =models.CharField(max_length=12)
    attendees =models.CharField(max_length=12)
    date =models.CharField(max_length=12)
    Time =models.CharField(max_length=12)
    message =models.CharField(max_length=150)
    drinks = models.CharField(max_length=150, null=True)
    beverages = models.CharField(max_length=150, null=True)
    service = models.CharField(max_length=150, null=True)
    Decoration = models.CharField(max_length=150, null=True)
    Budget=models.CharField(max_length=150, null=True)
    Output = models.CharField(max_length=200,null=True)
    Specialized = models.CharField(max_length=200,null=True)
    report =models.BooleanField(default=False, null=True)

class designing(models.Model):
    firstname = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phonenumber = models.CharField(max_length=12)
    address = models.CharField(max_length=12)
    city = models.CharField(max_length=12)
    country = models.CharField(max_length=12)
    area =  models.CharField(max_length=12)
    structure = models.CharField(max_length=50, null=True)
    ventilation = models.CharField(max_length=50, null=True)
    windows = models.CharField(max_length=50, null=True)
    budget =  models.CharField(max_length=12)
    message =  models.CharField(max_length=150, null=True)
    feet = models.CharField(max_length=100, null=True)
    walls = models.CharField(max_length=50, null=True)
    floor = models.CharField(max_length=50, null=True)
    Output = models.CharField(max_length=200, null=True)

    report = models.BooleanField(default=False)

