from django.db import models

# # Create your models here.
class Productapp(models.Model):
    pcode=models.IntegerField()
    pname=models.CharField(max_length=50)
    pdescription=models.CharField(max_length=50)
    pprice=models.IntegerField()