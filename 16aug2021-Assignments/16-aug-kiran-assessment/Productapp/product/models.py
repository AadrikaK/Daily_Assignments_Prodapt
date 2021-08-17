from django.db import models

# Create your models here.
class Product(models.Model):
    pname=models.CharField(max_length=50)
    pcode=models.IntegerField()
    description=models.CharField(max_length=50)
    price=models.IntegerField()