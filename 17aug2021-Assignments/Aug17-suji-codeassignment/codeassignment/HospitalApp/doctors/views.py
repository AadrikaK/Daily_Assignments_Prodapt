from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from doctors.serializers import DoctorsSerializer
import json
from doctors.models import Doctors
from rest_framework.parsers import JSONParser
from rest_framework import status


@csrf_exempt
def doctor_list(request):
    if(request.method=="GET"):
        doctors=Doctors.objects.all()
        doctors_serialize=DoctorsSerializer(doctors,many=True)
        return JsonResponse(doctors_serialize.data,safe=False)

@csrf_exempt
def doctor_details(request,fetchid):
    try:
        doctors=Doctors.objects.get(id=fetchid)
    except Doctors.DoesNotExist:
        return HttpResponse("Invalid Doctor Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        doctors_serialize=DoctorsSerializer(doctors)
        return JsonResponse(doctors_serialize.data,safe=False,status=status.HTTP_200_OK)

    if(request.method=="DELETE"):
        doctors.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)        
    
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        doctors_serialize=DoctorsSerializer(doctors,data=mydata)
        if(doctors_serialize.is_valid()):
            doctors_serialize.save()
            return JsonResponse(doctors_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(doctors_serialize.errors,status=status.HTTP_400_BAD_REQUEST)    

# Create your views here.
@csrf_exempt
def doctorAdd(request):
    if request.method=="POST":
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getSpecialization=request.POST.get("specialization")
        mydata={"name":getName,"address":getAddress,"specialization":getSpecialization}
        mydata=JSONParser().parse(request)
        doctors_serialize=DoctorsSerializer(data=mydata)
        if(doctors_serialize.is_valid()):
            doctors_serialize.save()
            return JsonResponse(doctors_serialize.data,status=status.HTTP_200_OK)
            #return HttpResponse("Success")
            
        #result=json.dumps(mydict)
        #return HttpResponse(result)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
        #result=json.dumps(mydict)
        #return HttpResponse(result)

    else:
        return HttpResponse("No get method allowed",status=status.HTTP_404_NOT_FOUND)

