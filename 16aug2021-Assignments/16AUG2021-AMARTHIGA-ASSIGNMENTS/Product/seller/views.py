from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from seller.serializers import SellerSerializer
from seller.models import Seller
# Create your views here.


@csrf_exempt
def viewseller(request):
    if (request.method =='GET'):
        sellers = Seller.objects.all()
        sel_serializers = SellerSerializer(sellers, many=True )
        return JsonResponse(sel_serializers.data, safe=False)



@csrf_exempt
def addseller(request):
    if (request.method == 'POST'):
        gets_name =request.POST.get('SellerName')
        gets_ID =request.POST.get('SellerID')
        gets_add =request.POST.get('SellerAdd')
        gets_phone =request.POST.get('SellerPhone')
        
        sell ={'SellerName':gets_name,'SellerID':gets_ID,'SellerAdd':gets_add, 'SellerPhone': gets_phone,};
        
        sell_serialize = SellerSerializer(data=sell)
        if(sell_serialize.is_valid()):
            sell_serialize.save()
            # return HttpResponse("Success")
            return JsonResponse(sell_serialize.data)
        
        else:
            return HttpResponse("Error in Serialization")
        
        # result =json.dumps(emp)
        #return HttpResponse(result)

    else:
        return HttpResponse('Hello, All! Welcome to Seller App page')