from django.db import models
from django.db.models.fields import CharField, IntegerField

# Create your models here.
class Employee(models.Model):
    name = models.CharField(max_length=50)
    Emp_ID = models.IntegerField()
    Emp_desi = CharField(max_length=50)
    Emp_salary = IntegerField()