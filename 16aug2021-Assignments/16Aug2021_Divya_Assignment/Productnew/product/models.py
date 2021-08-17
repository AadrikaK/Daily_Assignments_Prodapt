from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=50)
    pro_code = models.IntegerField()
    pro_desc = models.CharField(max_length=50)
    pro_price = models.IntegerField()
