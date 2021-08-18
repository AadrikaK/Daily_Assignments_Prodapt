from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from hotelapp.serializers import hotelSerializer
from hotelapp.models import hotel
from rest_framework.parsers import JSONParser
from rest_framework import status

# Create your views here. 

@csrf_exempt
def myhotel(reuest,fetchid):
    try:
        hotel1=hotel.objects.get(id=fetchid)
        if(request.method=="GET"):
            hotel_serializer=hotelSerializer(hotel)
            return JsonResponse(hotel_serializer.data,safe=False)

        if(request.method=="DELETE"):
            hotel1.delete()
            return HttpResponse("Deleted",status=status)

        if(request.method=="PUT"):
            mydic=JSONParser().parse(request)
            hotel_serialize=hotelSerializer(hotel1,data=mydic)
            if (hotel_serialize.is_valid()):
                hotel_serialize.save()
                return JsonResponse(hotel_serialize.data)
            else:
                return JsonResponse(hotel_serialize.errors)
    except hotel.Doesnotexist:
        return HttpResponse("invalid notes")
            

            


@csrf_exempt
def hotellist(request):
    if(request.method=="GET"):
        hotel1=hotel.objects.all()
        hotel_serializer=hotelSerializer(hotel1,many=True)
        return JsonResponse(hotel_serializer.data,safe=False)



@csrf_exempt
def Hotel(request):
    if(request.method=="POST"):
        mydic=JSONParser().parse(request)
        hotel_serialize=hotelSerializer(data=mydic)
        if (hotel_serialize.is_valid()):
            hotel_serialize.save()
            return JsonResponse(hotel_serialize.data)


    else:
        return HttpResponse("error")
