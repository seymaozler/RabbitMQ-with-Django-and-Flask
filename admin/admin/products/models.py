from django.db import models

class Product(models.Model):
    title = models.CharField(max_length=200)
    price = models.FloatField()
    image = models.CharField(max_length=300)
    likes = models.IntegerField(default=0)

class User(models.Model):
    pass