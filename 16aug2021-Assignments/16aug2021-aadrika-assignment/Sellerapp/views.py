from Sellerapp.serialize import Sellerserializers
from Sellerapp.models import Seller

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse,response
import json
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt
def view_Seller(request):
    if(request.method=='GET'):
        seller=Seller.objects.all()
        sellserialize=Sellerserializers(seller,many=True)
        return response.JsonResponse(sellserialize.data,safe=False)





@csrf_exempt
def add_Seller(request):
    if(request.method=="POST"):
        getname=request.POST.get("sname")
        getsid=request.POST.get("sid")
        getsadd=request.POST.get("sadd")
        getsphone=request.POST.get("sphone")
        mydata={"sname":getname,"sid":getsid,"sadd":getsadd,"sphone":getsphone}
        sellserialize=Sellerserializers(data=mydata)
        if(sellserialize.is_valid()):
            
            sellserialize.save()
            #return HttpResponse("success")
            return response.JsonResponse(sellserialize.data)
        else:
            return HttpResponse("error in serialization process")
    else:
        return HttpResponse("GET method is not runned")

