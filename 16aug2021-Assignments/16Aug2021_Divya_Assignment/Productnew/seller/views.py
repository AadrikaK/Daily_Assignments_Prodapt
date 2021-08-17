from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf  import csrf_exempt
import json
from seller.serializer import SellerSerializer
from seller.models import Seller

#Create your views here.
@csrf_exempt
def seller_list(request):
    if(request.method == "GET"):
        sellers = Seller.objects.all()
        seller_serialize = SellerSerializer(sellers,many = True)
        return JsonResponse(seller_serialize.data,safe= False)


@csrf_exempt
def addpage(request):
    if (request.method == "POST"):
        getName = request.POST.get("name")
        getID = request.POST.get("seller_ID")
        getadd = request.POST.get("seller_add")
        getphno = request.POST.get("seller_phno")
        mydata = {"name":getName,"seller_ID":getID,"seller_add":getadd,"seller_phno":getphno};
        seller_serialize=SellerSerializer(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        
        else:
            return HttpResponse("Error in serialization")

         
    else:
        return HttpResponse("thank you")