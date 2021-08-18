from django.db.models import fields
from rest_framework import serializers
from employeeapp.models import Employee

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields=('EmployeeName','EmployeeID', 'Designation', 'Salary')


