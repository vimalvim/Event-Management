from django.db import models

class tevents(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField(max_length=150)
    phonenumber = models.CharField(max_length=12)
    gender = models.CharField(max_length=10)
    password = models.CharField(max_length=150)

class events(models.Model):
    name = models.CharField(max_length=150)
    table = models.CharField(max_length=150)
    quantity = models.CharField(max_length=150)
    projector = models.CharField(max_length=150)
    quantity1 = models.CharField(max_length=150)
    mike = models.CharField(max_length=150)
    quantity2 = models.CharField(max_length=150)
    Tv = models.CharField(max_length=150)
    quantity3 = models.CharField(max_length=150)
    conditions = models.CharField(max_length=150)
    quantity4 = models.CharField(max_length=150)
    led = models.CharField(max_length=150)
    quantity5 = models.CharField(max_length=150)
    value = models.CharField(max_length=150)
    report = models.BooleanField(default=False, null=True)



class interior(models.Model):
    name = models.CharField(max_length=150)
    boards = models.CharField(max_length=150, null=True)
    quantity = models.CharField(max_length=150, null=True)
    woods = models.CharField(max_length=150, null=True)
    quantity1 = models.CharField(max_length=150, null=True)
    Tables = models.CharField(max_length=150, null=True)
    quantity2 = models.CharField(max_length=150, null=True)
    Designs = models.CharField(max_length=150, null=True)
    quantity3 = models.CharField(max_length=150, null=True)
    wallpapers = models.CharField(max_length=150, null=True)
    quantity4 = models.CharField(max_length=150, null=True)
    others = models.CharField(max_length=150, null=True)
    quantity5 = models.CharField(max_length=150, null=True)
    value = models.CharField(max_length=150, null=True)
    report = models.BooleanField(default=False, null=True)
