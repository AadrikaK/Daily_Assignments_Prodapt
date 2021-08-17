from django.http.response import JsonResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
import json
from productapp.serializers import ProductSerializer
from productapp.models import Product
# Create your views here.


@csrf_exempt
def viewpro(request):
    if (request.method =='GET'):
        products = Product.objects.all()
        pro_serializers = ProductSerializer(products, many=True )
        return JsonResponse(pro_serializers.data, safe=False)



@csrf_exempt
def addpro(request):
    if (request.method == 'POST'):
        getp_name =request.POST.get('ProductName')
        getp_ID =request.POST.get('ProductID')
        getp_Desc =request.POST.get('Description')
        getp_price =request.POST.get('ProductPrice')
        
        pro ={'ProductName':getp_name,'ProductID':getp_ID,'Description':getp_Desc, 'ProductPrice': getp_price,};
        
        pro_serialize = ProductSerializer(data=pro)
        if(pro_serialize.is_valid()):
            pro_serialize.save()
            # return HttpResponse("Success")
            return JsonResponse(pro_serialize.data)
        
        else:
            return HttpResponse("Error in Serialization")
        
        # result =json.dumps(emp)
        #return HttpResponse(result)

    else:
        return HttpResponse('Hello, All!')