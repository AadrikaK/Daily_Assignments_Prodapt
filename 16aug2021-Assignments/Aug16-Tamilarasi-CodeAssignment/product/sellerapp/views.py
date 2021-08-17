from sellerapp.models import Sellerapp
from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sellerapp.serializers import SellerappSerializer
from sellerapp.models import Sellerapp

# Create your views here.
@csrf_exempt
def mySellerList(request):
    if(request.method=="GET"):
        Sellersapp=Sellerapp.objects.all()
        sellerapp_serializer=SellerappSerializer(Sellersapp,many=True)
        return JsonResponse(sellerapp_serializer.data,safe=False)

@csrf_exempt
def mySellerPage(request):
    if(request.method=="POST"):
        getId=request.POST.get("sell_id")
        getName=request.POST.get("sell_name")
        getAddress=request.POST.get("sell_address")
        getMblno=request.POST.get("sell_mblno")
        dict={'sell_id':getId,'sell_name':getName,'sell_address':getAddress,'sell_mblno':getMblno}
        sellerapp_serialize=SellerappSerializer(data=dict)
        if(sellerapp_serialize.is_valid()):
            sellerapp_serialize.save()
            return JsonResponse(sellerapp_serialize.data)
        else:
            return HttpResponse("Error in Serialization")
  