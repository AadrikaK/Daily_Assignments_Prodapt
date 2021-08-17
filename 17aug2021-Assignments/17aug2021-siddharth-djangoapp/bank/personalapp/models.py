from django.db import models

class Personal(models.Model):
    
    account=models.CharField(max_length=50)
    custname=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    bal=models.CharField(max_length=50)
