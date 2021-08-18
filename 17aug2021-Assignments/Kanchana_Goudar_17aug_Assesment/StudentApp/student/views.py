from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from student.serializer import StudentSerializers
from student.models import Student
from rest_framework.parsers import JSONParser
from rest_framework import status
@csrf_exempt
def Student_details(request,fetchid):
    try:
        Students=Student.objects.get(id=fetchid)
    except Student.DoesNotExist:
        return HttpResponse("Invalid Student Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        student_serializer=StudentSerializers(Students)
        return JsonResponse(student_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        Students.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         student_serialize=StudentSerializers(Students,data=mydata)
         if (student_serialize.is_valid()):
             student_serialize.save()
             return JsonResponse(student_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(student_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def Studentview(request):
    if(request.method=="GET"):
        Students=Student.objects.all()
        Studentdata=StudentSerializers(Students,many=True)
        return JsonResponse(Studentdata.data,safe=False)

@csrf_exempt
def MyaddStudent(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        student_data=StudentSerializers(data=mydata)
        if(student_data.is_valid()):
            student_data.save()
            return JsonResponse(student_data.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
   
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)

