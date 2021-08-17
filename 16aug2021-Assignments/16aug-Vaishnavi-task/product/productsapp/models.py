from django.db import models

# Create your models here.
class productsdata(models.Model):
    product_name = models.CharField(max_length=50)
    product_code = models.IntegerField()
    product_description =models.CharField(max_length=50)
    product_price = models.IntegerField()