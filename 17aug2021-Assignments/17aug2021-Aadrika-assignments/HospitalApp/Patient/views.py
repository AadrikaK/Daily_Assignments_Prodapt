from django import http
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from Patient.serializers import PatientSerializer
from Patient.models import Patients
from rest_framework.parsers import JSONParser
from rest_framework import status





##################### adding NEW PATIENT to db ######################
@csrf_exempt
def addPat(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        patserialize=PatientSerializer(data=mydata)
        if (patserialize.is_valid()):
            patserialize.save() 
            return response.JsonResponse(patserialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization process of notes")

# ########### viewing all the PATIENTS #############################
@csrf_exempt
def viewPat(request):
    if (request.method=='GET'):
        pat1=Patients.objects.all()
        patientSerializer=PatientSerializer(pat1,many=True)
        return response.JsonResponse(patientSerializer.data, safe=False,status=status.HTTP_200_OK)

# ################# CRUD OPERATIONS ######################################
@csrf_exempt
def viewpatdetails(request,id):
    try:
        pat1=Patients.objects.get(id=id)
        if (request.method=='GET'):
            patientSerializer=PatientSerializer(pat1) 
            return response.JsonResponse(patientSerializer.data,safe=False,status=status.HTTP_200_OK)
        if (request.method=='DELETE'):
            pat1.delete()
            return HttpResponse("deleted patients")
        if (request.method=='PUT'):
            mydata=JSONParser().parse(request)
            patserial=PatientSerializer(pat1,data=mydata)
            if (patserial.is_valid()):
                patserial.save()
                return response.JsonResponse(patserial.data,status=status.HTTP_200_OK)
    except Patients.DoesNotExist:
        return HttpResponse("invalid ID for patient")


    
