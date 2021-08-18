from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from marks.serializer import MarksSerializers
from marks.models import Marks
from rest_framework.parsers import JSONParser
from rest_framework import status
@csrf_exempt
def Marks_details(request,fetchid):
    try:
        marks=Marks.objects.get(id=fetchid)
    except Marks.DoesNotExist:
        return HttpResponse("Invalid Marks Id",status=status.HTTP_404_NOT_FOUND)
    if (request.method=="GET"):
        marks_serializer=MarksSerializers(marks)
        return JsonResponse(marks_serializer.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=="DELETE"):
        marks.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)
    if (request.method=="PUT"):
         mydata=JSONParser().parse(request)
         marks_serialize=MarksSerializers(marks,data=mydata)
         if (marks_serialize.is_valid()):
             marks_serialize.save()
             return JsonResponse(marks_serialize.data,status=status.HTTP_200_OK)
         else:
              return JsonResponse(marks_serialize.errors,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
def Marksview(request):
    if(request.method=="GET"):
        marks=Marks.objects.all()
        marksdata=MarksSerializers(marks,many=True)
        return JsonResponse(marksdata.data,safe=False)

@csrf_exempt
def Myaddmarks(request):
    if(request.method=="POST"):
        mydata=JSONParser().parse(request)
        marks_data=MarksSerializers(data=mydata)
        if(marks_data.is_valid()):
            marks_data.save()
            return JsonResponse(marks_data.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
   
    else:
        return HttpResponse("No get method is allowed",status=status.HTTP_404_NOT_FOUND)