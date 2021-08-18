from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from courierApp.serializers import CourierSerializers
from courierApp.models import Courier
from rest_framework.parsers import JSONParser 
from rest_framework import status


@csrf_exempt
def addCourier(request):
    if(request.method == "POST"):
        mydict = JSONParser().parse(request)
        courierSerialize = CourierSerializers(data = mydict)
        if (courierSerialize.is_valid()):
            courierSerialize.save()   
            return JsonResponse(courierSerialize.data, status=status.HTTP_200_OK)

        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("GET Method not allowed",status=status.HTTP_404_NOT_FOUND)



@csrf_exempt
def listCourier(request):
    if (request.method == "GET"):
        courier = Courier.objects.all()
        courier_serializers = CourierSerializers(courier, many= True)
        return JsonResponse(courier_serializers.data, safe =False)


@csrf_exempt
def  courierData(request,cid):
    try:
        courier = Courier.objects.get(cid = cid)
        if(request.method == "GET"):
            courier_serializer = CourierSerializers(courier)
            return JsonResponse(courier_serializer.data, safe = False, status=status.HTTP_200_OK)    

        if (request.method == "DELETE"):
            courier.delete()
            return HttpResponse("Deleted", status=status.HTTP_204_NO_CONTENT)

        if (request.method == "PUT"):
            mydict = JSONParser().parse(request)

            courier_serialize = CourierSerializers(courier,data = mydict)
            if (courier_serialize.is_valid()):
                courier_serialize.save()    
                return JsonResponse(courier_serialize.data, status=status.HTTP_200_OK)


    except Courier.DoesNotExist:
        return HttpResponse("Invalid Courier ID",status=status.HTTP_404_NOT_FOUND)

        
