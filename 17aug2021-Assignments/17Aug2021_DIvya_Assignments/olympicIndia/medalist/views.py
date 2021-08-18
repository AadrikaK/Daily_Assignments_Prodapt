from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from medalist.serializer import MedalistSerializer
from medalist.models import Medalist
from rest_framework.parsers import JSONParser
from rest_framework import status
# Create your views here.
@csrf_exempt
def addpage(request):
    if(request.method=="POST"):
        mydata = JSONParser().parse(request)
        medal_serialize = MedalistSerializer(data=mydata)
        if(medal_serialize.is_valid()):
            medal_serialize.save()
            return JsonResponse(medal_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_404_NOT_FOUND)
    else:
        return HttpResponse("Bye Bye")

@csrf_exempt
def medal_list(request):
    if(request.method=="GET"):
        medals = Medalist.objects.all()
        medal_serialize = MedalistSerializer(medals,many = True)
        return JsonResponse(medal_serialize.data,safe=False)

@csrf_exempt
def medalpage(request,id):
    try:
        medals = Medalist.objects.get(id=id)
    except Medalist.DoesNotExist:
        return HttpResponse("Invalid medalist Id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        medal_serialize = MedalistSerializer(medals)
        return JsonResponse(medal_serialize.data,safe=False,status=status.HTTP_200_OK)
    if (request.method == "PUT"):
        mydata = JSONParser().parse(request)
        medal_serialize = MedalistSerializer(medals,data=mydata)
        if (medal_serialize.is_valid()):
            medal_serialize.save()
            return JsonResponse(medal_serialize.data,status=status.HTTP_200_OK)
    if(request.method == "DELETE"):
        medals.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)

