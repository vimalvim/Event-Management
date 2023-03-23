from django.db import models

class event(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phonenumber = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=150)
