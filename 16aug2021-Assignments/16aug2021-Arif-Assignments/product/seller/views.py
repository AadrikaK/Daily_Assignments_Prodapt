from django.shortcuts import render
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller

@csrf_exempt
def seller_list(request):
    if(request.method=="GET"):
        k=Seller.objects.all()
        seller_serializer=SellerSerializer(k,many=True)
        return JsonResponse(seller_serializer.data,safe=False)
@csrf_exempt
def seller_create(request):
    if (request.method=="POST"):
        getName=request.POST.get("name")
        getscode=request.POST.get("scode")
        getsaddress=request.POST.get("sadd")
        getphone=request.POST.get("snum")
        mydata={"name":getName,"scode":getscode,"sadd":getsaddress,"snum":getphone}
        seller_serialize=SellerSerializer(data=mydata)
        #result=json.dumps(mydict)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("error in serialization")
    else:
        return HttpResponse("no get")



