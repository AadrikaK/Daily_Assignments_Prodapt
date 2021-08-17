from django.db import models

# Create your models here.
class Productapp(models.Model):
    pro_code=models.IntegerField()
    pro_name=models.CharField(max_length=50)
    pro_description=models.CharField(max_length=50)
    pro_price=models.IntegerField()
