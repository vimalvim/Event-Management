from django.db import models

class fevents(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phonenumber = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=150)

class eventcompany(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    budget = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    services = models.CharField(max_length=150, null=True)
    specialized = models.CharField(max_length=150, null=True)
    experience = models.CharField(max_length=150, null=True)
    employees = models.CharField(max_length=150, null=True)
    report = models.BooleanField(default=False)


class Interiorcompany(models.Model):
    name = models.CharField(max_length=150)
    address = models.CharField(max_length=150)
    services = models.CharField(max_length=150)
    budget = models.CharField(max_length=150)
    number = models.CharField(max_length=150)
    specialized = models.CharField(max_length=150, null=True)
    experience = models.CharField(max_length=150, null=True)
    employees = models.CharField(max_length=150, null=True)
    report = models.BooleanField(default=False)

