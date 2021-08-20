from django.db import models

# Create your models here.

class Product(models.Model):
    pname=models.CharField(max_length=50)
    pcode=models.IntegerField()
    pdescription=models.CharField(max_length=50)
    pprice=models.IntegerField()