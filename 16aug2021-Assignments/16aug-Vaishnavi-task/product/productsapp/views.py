from django.shortcuts import render
from productsapp.models import productsdata
# Create your views here.
from productsapp.serializer import product_Serializer
from django.http.response import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt




@csrf_exempt 
def product_list(request):
    if(request.method == "GET"):
        product1 = productsdata.objects.all()
        pro_Serializer= product_Serializer(product1, many=True)
        return JsonResponse(pro_Serializer.data, safe=False)




@csrf_exempt
def product_details(request):
    if (request.method=="POST"):
        getproductName=request.POST.get("name")
        getproductcode=request.POST.get("code")
        getproductdescription=request.POST.get("description")
        getproductprice=request.POST.get("price")
        product_data= {'product_name':getproductName ,'product_code':getproductcode ,'product_description':getproductdescription , 'product_price':getproductprice} 
        product_serialize = product_Serializer(data=product_data)
        if (product_serialize.is_valid()):
            product_serialize.save()
            return JsonResponse(product_serialize.data) 
    else:
        return HttpResponse('no get method')