from django.db import models

class Product(models.Model):
    pname=models.CharField(max_length=50)
    pcode=models.IntegerField()
    pdescp=models.CharField(max_length=50)
    pprice=models.IntegerField()