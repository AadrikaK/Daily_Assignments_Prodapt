from django.http.response import JsonResponse
from productapp.models import Productapp
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductappSerializer
from productapp.models import Productapp
# Create your views here.
@csrf_exempt
def productapp_list(request):
    if(request.method=="GET"):
        productsapp=Productapp.objects.all()
        productapp_serializer=ProductappSerializer(productsapp,many=True)
        return JsonResponse(productapp_serializer.data,safe=False)

@csrf_exempt
def productapp_create(request):
    if(request.method=="POST"):
        getpcode=(request.POST.get("pcode"))
        getpname=(request.POST.get("pname"))
        getpdescription=request.POST.get("pdescription")
        getpprice=request.POST.get("pprice")
        mydata={"pcode":getpcode,"pname":getpname,"pdescription":getpdescription,"pprice":getpprice}
        productapp_serialize=ProductappSerializer(data=mydata)
        if (productapp_serialize.is_valid()):
            productapp_serialize.save()
            # return HttpResponse("Sucess")
            return JsonResponse(productapp_serialize.data)
        else:
            return HttpResponse("Error in serilization")
    # else:
    #     return HttpResponse("GET METHOD")