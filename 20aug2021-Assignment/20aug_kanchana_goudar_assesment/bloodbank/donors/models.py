from django.db import models

# Create your models here.
class Donor(models.Model):
    Blood_group=models.CharField(max_length=50)
    Name=models.CharField(max_length=50)
    Adress=models.CharField(max_length=50)
    Pincode=models.CharField(max_length=50)
    Mobileno=models.CharField(max_length=50)
    Last_donated_date=models.CharField(max_length=50)
