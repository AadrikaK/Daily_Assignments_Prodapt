from django.db import models

class Vegitableapp1(models.Model):
    vegitableid = models.IntegerField()
    vegitablename = models.CharField(max_length=20)
    vegitabledescription = models.CharField(max_length=100)
    vegitableprice = models.IntegerField()

