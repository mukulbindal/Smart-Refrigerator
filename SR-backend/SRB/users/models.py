from django.db import models


# Create your models here.

class Refrigerator(models.Model):
    FID = models.CharField(primary_key=True, max_length=52)
    IP = models.CharField(max_length=52)


class User(models.Model):
    UID = models.CharField(primary_key=True, max_length=52)
    UNAME = models.CharField(max_length=100)
    password = models.CharField(max_length=200)
    FID = models.ForeignKey(Refrigerator, on_delete=models.SET_NULL, null=True)
    token = models.CharField(max_length=200, default="none")



