from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from SellerApp.serializers import SellerSerializer
from SellerApp.models import Seller

# Create your views here. 
@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        seller1=Seller.objects.all()
        seller_serializer=SellerSerializer(seller1,many=True)
        return JsonResponse(seller_serializer.data,safe=False)



@csrf_exempt
def seller(request):
    if(request.method=="POST"):
        getname=request.POST.get("sname")
        getid=request.POST.get("sid")
        getaddress=request.POST.get("saddress")
        getnum=request.POST.get("snum")
        mydict={"sname":getname,"sid":getid,"saddress":getaddress,"snum":getnum}
        seller_serialize=SellerSerializer(data=mydict)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)


    else:
        return HttpResponse("error")