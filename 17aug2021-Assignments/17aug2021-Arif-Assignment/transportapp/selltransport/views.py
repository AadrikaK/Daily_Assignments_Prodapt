from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from selltransport.serializers import SellerSerializer
from selltransport.models import Seller
from rest_framework.parsers import JSONParser
from rest_framework import status

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        k=Seller.objects.all()
        seller_serializer=SellerSerializer(k,many=True)
        return JsonResponse(seller_serializer.data,safe=False)


@csrf_exempt
def seller_details(request,fetchid):
    try:
        k=Seller.objects.get(id=fetchid)
    except Seller.DoesNotExist:
        return HttpResponse("invalid product id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        seller_serializer=SellerSerializer(k)
        return JsonResponse(seller_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        k.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(k,data=mydata)
        
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)


@csrf_exempt
def seller_create(request):
    if (request.method=="POST"):
        mydata=JSONParser().parse(request)
        seller_serialize=SellerSerializer(data=mydata)
        
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)




