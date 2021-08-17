from django.http.response import JsonResponse
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
import json
from product.serializers import ProductsSerializers
from product.models import Products


@csrf_exempt
def products_list(request):
    if (request.method == "GET"):
        products = Products.objects.all()
        product_serializers = ProductsSerializers(products, many= True)
        return JsonResponse(product_serializers.data, safe =False)
        




@csrf_exempt
def products_add(request):
    if(request.method == "POST"):
        getprodcode = request.POST.get("prodcode")
        getprodname = request.POST.get("prodname")
        getproddesc = request.POST.get("proddesc")
        getprodprice = request.POST.get("prodprice")

        mydict = {"prodcode":getprodcode, "prodname":getprodname,"proddesc":getproddesc,"prodprice":getprodprice}

        product_serialize = ProductsSerializers(data = mydict)
        if (product_serialize.is_valid()):

            product_serialize.save()   
            return JsonResponse(product_serialize.data)
        else:
            return HttpResponse("Error in Serialization")



        x = json.dumps(mydict)
        return HttpResponse(x)

    else:
        return HttpResponse("GET Method not allowed")        
