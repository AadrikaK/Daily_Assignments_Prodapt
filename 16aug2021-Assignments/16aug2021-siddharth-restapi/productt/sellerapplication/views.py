from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt
from sellerapplication.serializers import SellerSerializers
from sellerapplication.models import Seller
# Create your views here.
@csrf_exempt
def AddSeller(request):
    if(request.method=="POST"):
        s_name=request.POST.get("sname")
        s_id=request.POST.get("sid")
        s_address=request.POST.get("sadd")
        s_phone=request.POST.get("sphone")
        mydict={"sname":s_name,"sid":s_id,"sadd":s_address,"sphone":s_phone}
        seller_serialize=SellerSerializers(data=mydict)
        if(seller_serialize.is_valid()):
            seller_serialize.save()
            #return HttpResponse("success")
            return response.JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("GET method got runned")

@csrf_exempt
def ViewSeller(request):
    if(request.method=='GET'):
        seller1=Seller.objects.all()
        seller_serialize=SellerSerializers(seller1,many=True)
        return response.JsonResponse(seller_serialize.data,safe=False)
