from django.shortcuts import render
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework import status
from django.http import HttpResponse
from django.http.response import JsonResponse

from seller.models import sellers
from seller.serializer import selSerializer

# Create your views here.
def regseller(request):
    return render(request, 'seller.html')

@csrf_exempt
def addseller(request):
    if(request.method =='POST'):
        selldata = JSONParser().parse(request)
        sell_serialize = selSerializer(data=selldata)

        if(sell_serialize.is_valid()):
            sell_serialize.save()
            return JsonResponse(sell_serialize.data, status = status.HTTP_200_OK)

        else:
            return HttpResponse("Error in Serialization", status = status.HTTP_400_BAD_REQUEST)

    else:
        return HttpResponse("Welcome all to product page!")

@csrf_exempt
def viewseller(request):
    if(request.method == 'GET'):
        sell=sellers.objects.all()
        sell_serializer = selSerializer(sell, many=True)
        return JsonResponse(sell_serializer.data, safe=False)
        
    else:
        return HttpResponse("Welcome to view shop details!")

@csrf_exempt
def sellerdetails(request, id):
    try:
        sell = sellers.objects.get(id = id)
        if (request.method == 'GET'):
            sell_serialize = selSerializer(sell)
            return JsonResponse(sell_serialize.data, safe = False, status=status.HTTP_200_OK)
        if (request.method == "DELETE"):
                    sell.delete()
                    return HttpResponse("Content Deleted", status=status.HTTP_204_NO_CONTENT)
        if(request.method =='PUT'):
             seldata = JSONParser().parse(request)
             sell_serialize = selSerializer(sell, data=seldata)
             if(sell_serialize.is_valid()):
                 sell_serialize.save()
                 return JsonResponse(sell_serialize.data, status=status.HTTP_200_OK)

    except sellers.DoesNotExist:
        return HttpResponse("Invalid Employee Id", status=status.HTTP_400_BAD_REQUEST)

