from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    image = models.CharField(max_length=2083)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Offer(models.Model):
    code = models.CharField(max_length=10)
    description = models.TextField()
    discount = models.FloatField()