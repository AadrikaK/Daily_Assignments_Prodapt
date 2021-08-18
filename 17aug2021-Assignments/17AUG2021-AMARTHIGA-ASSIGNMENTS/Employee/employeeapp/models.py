from django.db import models

# Create your models here.
class Employee(models.Model):
    EmployeeName= models.CharField(max_length = 50)
    EmployeeID= models.IntegerField()
    Designation= models.CharField(max_length = 50)
    Salary= models.IntegerField()
