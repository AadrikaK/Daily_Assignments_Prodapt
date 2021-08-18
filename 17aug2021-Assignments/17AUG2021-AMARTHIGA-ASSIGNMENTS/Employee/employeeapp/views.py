from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from employeeapp.serializer import EmployeeSerializer
from employeeapp.models import Employee
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def employee_details(request, id):
    try: 
        employees = Employee.objects.get(id=id)
        if (request.method == 'GET'):
            employee_serializer = EmployeeSerializer(employees)
            return JsonResponse(employee_serializer.data, safe = False, status=status.HTTP_200_OK)

        if (request.method == "DELETE"):
                    employees.delete()
                    return HttpResponse("Deleted", status=status.HTTP_204_NO_CONTENT)
        if(request.method =='PUT'):
             mydata = JSONParser().parse(request)
             emp_serialize = EmployeeSerializer(employees, data=mydata)
             if(emp_serialize.is_valid()):
                 emp_serialize.save()
                 return JsonResponse(emp_serialize.data, status=status.HTTP_200_OK)
            

    except Employee.DoesNotExist:
        return HttpResponse("Invalid Employee Id", status=status.HTTP_400_BAD_REQUEST)
    

    


@csrf_exempt
def viewemp(request):
    if (request.method =='GET'):
        employees = Employee.objects.all()
        emp_serializers = EmployeeSerializer(employees, many=True )
        return JsonResponse(emp_serializers.data, safe=False)






@csrf_exempt
def addemp(request):
    if (request.method == 'POST'):
        # getE_name =request.POST.get('EmployeeName')
        # getID =request.POST.get('EmployeeID')
        # getDesig =request.POST.get('Designation')
        # getE_Salary =request.POST.get('Salary')
        
        # emp ={'EmployeeName': getE_name,'EmployeeID':getID,'Designation':getDesig, 'Salary': getE_Salary,};
        
        mydata = JSONParser().parse(request)
        emp_serialize = EmployeeSerializer(data=mydata)
        if(emp_serialize.is_valid()):
            emp_serialize.save()
            # return HttpResponse("Success")
            return JsonResponse(emp_serialize.data, status=status.HTTP_200_OK)

        
        else:
            return HttpResponse("Error in Serialization", status=status.HTTP_400_BAD_REQUEST)
        
        # result =json.dumps(emp)
        #return HttpResponse(result)

    else:
        return HttpResponse('Hi, Welcome')