from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from employeeapp.serializer import EmployeeSerializer
from employeeapp.models import Employee

@csrf_exempt
def viewemp(request):
    if (request.method =='GET'):
        employees = Employee.objects.all()
        emp_serializers = EmployeeSerializer(employees, many=True )
        return JsonResponse(emp_serializers.data, safe=False)






@csrf_exempt
def addemp(request):
    if (request.method == 'POST'):
        getE_name =request.POST.get('EmployeeName')
        getID =request.POST.get('EmployeeID')
        getDesig =request.POST.get('Designation')
        getE_Salary =request.POST.get('Salary')
        
        emp ={'EmployeeName': getE_name,'EmployeeID':getID,'Designation':getDesig, 'Salary': getE_Salary,};
        
        emp_serialize = EmployeeSerializer(data=emp)
        if(emp_serialize.is_valid()):
            emp_serialize.save()
            # return HttpResponse("Success")
            return JsonResponse(emp_serialize.data)

        
        else:
            return HttpResponse("Error in Serialization")
        
        # result =json.dumps(emp)
        #return HttpResponse(result)

    else:
        return HttpResponse('Hi, Welcome')