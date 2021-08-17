from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from sellerapp.serializers import SellerSerializers
from sellerapp.models import Seller

@csrf_exempt
def seller_list(request):
    if (request.method=="GET"):
        seller=Seller.objects.all()
        seller_serialize=SellerSerializers(seller,many=True)
        return JsonResponse(seller_serialize.data,safe=False)


@csrf_exempt
def Myaddpage(request):
    if(request.method=="POST"):
        getsid=request.POST.get("Sid")
        getsname=request.POST.get("Sname")
        getadress=request.POST.get("Adress")
        getphno=request.POST.get("Phno")
        mydata={"Sid":getsid,"Sname":getsname,"Adress":getadress,"Phno":getphno}
        seller_serialize=SellerSerializers(data=mydata)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("Error in serialization")
        
    else:
        return HttpResponse("No get method is allowed")

