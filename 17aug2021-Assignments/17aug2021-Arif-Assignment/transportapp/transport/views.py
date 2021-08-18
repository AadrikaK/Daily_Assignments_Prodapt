from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from transport.serializers import TransportSerializer
from transport.models import Transport
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def transport_list(request):
    if(request.method=="GET"):
        k=Transport.objects.all()
        transport_serializer=TransportSerializer(k,many=True)
        return JsonResponse(transport_serializer.data,safe=False)


@csrf_exempt
def transport_details(request,fetchid):
    try:
        k=Transport.objects.get(id=fetchid)
    except Transport.DoesNotExist:
        return HttpResponse("invalid product id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        transport_serializer=TransportSerializer(productes)
        return JsonResponse(transport_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        k.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        transport_serialize=TransportSerializer(k,data=mydata)
        
        if (transport_serialize.is_valid()):
            transport_serialize.save()
            return JsonResponse(transport_serialize.data,status=status.HTTP_200_OK)


@csrf_exempt
def transport_create(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        transport_serialize=TransportSerializer(data=mydata)
        
        if (transport_serialize.is_valid()):
            transport_serialize.save()
            return JsonResponse(transport_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)



