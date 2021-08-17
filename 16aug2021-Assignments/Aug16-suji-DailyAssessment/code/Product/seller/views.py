from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller

# Create your views here.

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        sellers=Seller.objects.all()
        seller_serialize=SellerSerializer(sellers,many=True)
        return JsonResponse(seller_serialize.data,safe=False)



@csrf_exempt
def sellerAddPage(request):
    if request.method=="POST":
        getName=request.POST.get("name")
        getAddress=request.POST.get("address")
        getId=request.POST.get("sid")
        getNumber=request.POST.get("number")
        mydata={"name":getName,"address":getAddress,"sid":getId,"number":getNumber};
        #result=json.dumps(mydict)
        #return HttpResponse(result)
        seller_serialize=SellerSerializer(data=mydata)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("Error in serialization")

    else:     
        return HttpResponse("No get method allowed")   

