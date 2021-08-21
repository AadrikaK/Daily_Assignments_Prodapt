from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from shop.models import shops
from shop.serializer import shopSerializer


# Create your views here.
def register(request):
    return render(request, 'reg.html')

@csrf_exempt
def addshop(request):
    if(request.method =='POST'):
        shopdata = JSONParser().parse(request)
        shop_serialize = shopSerializer(data=shopdata)

        if(shop_serialize.is_valid()):
            shop_serialize.save()
            return JsonResponse(shop_serialize.data, status = status.HTTP_200_OK)

        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome all!")

@csrf_exempt
def viewshop(request):
    if(request.method == 'GET'):
        shop=shops.objects.all()
        shop_serializer = shopSerializer(shop, many=True)
        return JsonResponse(shop_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view shop details!")

@csrf_exempt
def shopdetails(request, id):
    try:
        shop = shops.objects.get(id = id)
        if (request.method == 'GET'):
            shops_serialize = shopSerializer(shop)
            return JsonResponse(shops_serialize.data, safe = False, status=status.HTTP_200_OK)
        if (request.method == "DELETE"):
                    shop.delete()
                    return HttpResponse("Content Deleted", status=status.HTTP_204_NO_CONTENT)
        if(request.method =='PUT'):
             shopdata = JSONParser().parse(request)
             shop_serialize = shopSerializer(shop, data=shopdata)
             if(shop_serialize.is_valid()):
                 shop_serialize.save()
                 return JsonResponse(shop_serialize.data, status=status.HTTP_200_OK)

        
    except shops.DoesNotExist:
        return HttpResponse("Invalid Employee Id", status=status.HTTP_400_BAD_REQUEST)

