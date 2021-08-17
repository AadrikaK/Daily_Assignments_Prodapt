from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from employee.serialize import EmployeeSerializer
from employee.models import Employee
# Create your views here.
@csrf_exempt
def employee_list(request):
    if(request.method == "GET"):
        employees = Employee.objects.all()
        employee_serialize = EmployeeSerializer(employees,many = True)
        return JsonResponse(employee_serialize.data,safe= False)




@csrf_exempt
def addpage(request):
    if (request.method == "POST"):
        getName = request.POST.get("name")
        getid = request.POST.get("Emp_ID")
        getdesi = request.POST.get("Emp_desi")
        getesalary = request.POST.get("Emp_salary")
        mydata = {"name":getName,"Emp_ID":getid,"Emp_desi":getdesi,"Emp_salary":getesalary};
        employee_serialize=EmployeeSerializer(data=mydata)
        if(employee_serialize.is_valid()):
            employee_serialize.save()
            return JsonResponse(employee_serialize.data)
            #return HttpResponse("success")
        else:
            return HttpResponse("Error in serialization")

        
    else:
        return HttpResponse("thank you")
