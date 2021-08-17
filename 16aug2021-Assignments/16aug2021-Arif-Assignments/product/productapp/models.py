from django.db import models

class Product(models.Model):
    name=models.CharField(max_length=50)
    pcode=models.IntegerField()
    pdes=models.CharField(max_length=25)
    pprice=models.IntegerField()