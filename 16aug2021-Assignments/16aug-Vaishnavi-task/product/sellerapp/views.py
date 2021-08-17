
from django.shortcuts import render
from sellerapp.models import sellersdata
from sellerapp.serializers import seller_Serializer
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt 
def seller_list(request):
    if(request.method == "GET"):
        seller1 = sellersdata.objects.all()
        seller_Serialize= seller_Serializer(seller1, many=True)
        return JsonResponse(seller_Serialize.data, safe=False)




@csrf_exempt
def seller_details(request):
    if (request.method=="POST"):
        getsellerName=request.POST.get("name")
        getsellerid=request.POST.get("id")
        getselleraddress=request.POST.get("address")
        getsellerphoneno=request.POST.get("phoneno")
        seller_data= {'seller_name':getsellerName ,'seller_id':getsellerid ,'seller_address':getselleraddress , 'seller_phoneno':getsellerphoneno} 
        seller_serialize = seller_Serializer(data=seller_data)
        if (seller_serialize.is_valid()):
            seller_serialize.save()
            return JsonResponse(seller_serialize.data) 
    else:
        return HttpResponse('no get method')