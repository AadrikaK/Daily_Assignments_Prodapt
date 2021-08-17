from seller.models import Sellers
from seller.seller_serializer import SellerSerializers
from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from seller.models import Sellers


@csrf_exempt
def sellers_list(request):
    if (request.method == "GET"):
        seller = Sellers.objects.all()
        seller_serializers = SellerSerializers(seller, many= True)
        return JsonResponse(seller_serializers.data, safe =False)
        




@csrf_exempt
def sellers_add(request):
    if(request.method == "POST"):
        getsellerid = request.POST.get("sellerid")
        getsellername = request.POST.get("sellername")
        getselleraddr = request.POST.get("selleraddress")
        getsellerphno = request.POST.get("sellerphno")

        mydict1 = {"sellerid":getsellerid, "sellername":getsellername,"selleraddress":getselleraddr,"sellerphno":getsellerphno}

        seller_serialize = SellerSerializers(data = mydict1)
        if (seller_serialize.is_valid()):

            seller_serialize.save()   
            return JsonResponse(seller_serialize.data)
        else:
            return HttpResponse("Error in Serialization")



        x = json.dumps(mydict)
        return HttpResponse(x)

    else:
        return HttpResponse("GET Method not allowed")        
