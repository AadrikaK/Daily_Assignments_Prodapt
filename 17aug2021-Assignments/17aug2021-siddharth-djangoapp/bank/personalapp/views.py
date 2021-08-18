from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from personalapp.serializers import PersonalSerializers
from personalapp.models import Personal
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def add_Personal(request):
    if(request.method=="POST"):
        mydict=JSONParser().parse(request)
        personal_serialize=PersonalSerializers(data=mydict)
        if(personal_serialize.is_valid()):
            personal_serialize.save()
            return response.JsonResponse(personal_serialize.data,status=status.HTTP_200_OK)

        else:
            return HttpResponse("error in serialization part of code",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("GET method executed")

@csrf_exempt
def show_Personals(request):
    if(request.method=='GET'):
        p1=Personal.objects.all()
        personal_serialize=PersonalSerializers(p1,many=True)
        return response.JsonResponse(personal_serialize.data,safe=False,status=status.HTTP_200_OK)

@csrf_exempt
def view_a_Personal(request,id):
    try:
        p1=Personal.objects.get(id=id)
    except:
        return HttpResponse("Invalid personal id")
    
    if(request.method=='GET'):
        
        personal_serialize=PersonalSerializers(p1)
        return response.JsonResponse(personal_serialize.data,safe=False)
    
    if(request.method=='PUT'):
        mydict=JSONParser().parse(request)
        personal_serialize=PersonalSerializers(p1,data=mydict)
        if (personal_serialize.is_valid()):
            personal_serialize.save()
            return response.JsonResponse(personal_serialize.data)

    if(request.method=='DELETE'):
        p1.delete()
        return HttpResponse("Personal deleted")

