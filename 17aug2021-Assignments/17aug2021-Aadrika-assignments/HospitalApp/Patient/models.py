from django.db import models
# Create your models here.
class Patients(models.Model):
    pname=models.CharField(max_length=50)
    padd=models.CharField(max_length=50)
    pmob=models.CharField(max_length=50)
    
