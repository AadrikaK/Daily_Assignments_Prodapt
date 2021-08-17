from django.db import models

# Create your models here.
class Product(models.Model):
    ProductName = models.CharField(max_length = 50)
    ProductID = models.IntegerField()
    Description = models.CharField(max_length = 50)
    ProductPrice = models.IntegerField()
