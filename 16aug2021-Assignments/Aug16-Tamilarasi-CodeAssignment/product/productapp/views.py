import productapp
from productapp.models import Productapp
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductappSerializer
from productapp.models import Productapp

# Create your views here.
@csrf_exempt
def myProductList(request):
    if(request.method=="GET"):
        productsapp=Productapp.objects.all()
        productapp_serializer=ProductappSerializer(productsapp,many=True)
        return JsonResponse(productapp_serializer.data,safe=False)

@csrf_exempt
def myProductPage(request):
    if(request.method=="POST"):
        getCode=request.POST.get("pro_code")
        getName=request.POST.get("pro_name")
        getDescription=request.POST.get("pro_description")
        getPrice=request.POST.get("pro_price")
        dict={'pro_code':getCode,'pro_name':getName,'pro_description':getDescription,'pro_price':getPrice}
        productapp_serialize=ProductappSerializer(data=dict)
        if(productapp_serialize.is_valid()):
            productapp_serialize.save()
            #return HttpResponse("Success")
            return JsonResponse(productapp_serialize.data)
        else:
            return HttpResponse("Error in Serialization")
  