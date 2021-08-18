from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from bankapp.serializers import BankSerializers
from bankapp.models import Banking
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def add_Staff(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        bank_serialize=BankSerializers(data=mydict)
        if(bank_serialize.is_valid()):
            bank_serialize.save()
            return response.JsonResponse(bank_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("error in serialization part of code",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method executed")

@csrf_exempt
def show_Staff(request):
    if(request.method=='GET'):
        b1=Banking.objects.all()
        bank_serialize=BankSerializers(b1,many=True)
        return response.JsonResponse(bank_serialize.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def view_a_Staff(request,id):
    try:
        b1=Banking.objects.get(id=id)
    except:
        return HttpResponse("Invalid staff id")
    
    if(request.method=='GET'):
        
        bank_serialize=BankSerializers(b1)
        return response.JsonResponse(bank_serialize.data,safe=False)
    
    if(request.method=='PUT'):
        mydict=JSONParser().parse(request)
        bank_serialize=BankSerializers(b1,data=mydict)
        if (bank_serialize.is_valid()):
            bank_serialize.save()
            return response.JsonResponse(bank_serialize.data)

    if(request.method=='DELETE'):
        b1.delete()
        return HttpResponse("staff deleted")
