from django.shortcuts import render,redirect
from django.http import HttpResponse,JsonResponse,response
from django.views.decorators.csrf import csrf_exempt
import json
from VoizFonica.models import Admin, Dongle, Postpaid, Prepaid, Queries
from VoizFonica.serializers import AdminSerializer, QueriesSerializer
from VoizFonica.serializers import PrepaidSerializer
from VoizFonica.serializers import PostpaidSerializer
from VoizFonica.serializers import DongleSerializer
from VoizFonica.models import Customer
from VoizFonica.serializers import CustomerSerializer
from VoizFonica.models import Prepaidinvoice
from VoizFonica.serializers import PrepaidinvoiceSerializer
from django.contrib.auth import logout

from rest_framework.parsers import JSONParser
from rest_framework import status
import requests

from VoizFonicaTelecom.settings import EMAIL_HOST_USER
from django.shortcuts import render,redirect
from django.core.mail import send_mail,EmailMessage

def adminPage(request):
    return render(request,"header1.html")

def loginview(request):
    return render(request,"login.html")

def prepaidview(request):
    return render(request,'addprepaid.html')

def postpaidview(request):
    return render(request,'addpostpaid.html')

def dongleview(request):
    return render(request,'adddongle.html')
    
# def registeradmin(request):
#     return render(request,'register.html')

def previewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/VoizFonica/viewall1/").json
    return render(request,'viewprepaid.html',{"data":fetchdata})

def postviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/VoizFonica/viewall2/").json
    return render(request,'viewpostpaid.html',{"data":fetchdata})

def dongleviewss(request):
    fetchdata=requests.get("http://127.0.0.1:8000/VoizFonica/viewall3/").json
    return render(request,'viewdongle.html',{"data":fetchdata})

def presearch(request):
    return render(request,'searchprepaid.html')

def postsearch(request):
    return render(request,'searchpostpaid.html')

def donglesearch(request):
    return render(request,'searchdongle.html')
def preupdate(request):
    return render(request,'updateprepaid.html')

def postupdate(request):
    return render(request,'updatepostpaid.html')

def dongleupdate(request):
    return render(request,'updatedongle.html')


def dongledelete(request):
    return render(request,'deletedongle.html')
def prepaiddelete(request):
    return render(request,'deleteprepaid.html')
def postpaiddelete(request):
    return render(request,'deletepostpaid.html')

# @csrf_exempt
# def searchapi(request):
#     try:
#         get=request.POST.get("bno")
#         getbno=Flat.objects.filter(bno=getbuildingno)
#         flat_serializer=FlatSerializer(getbno,many=True)
        
#         return render(request,"search.html",{"data":flat_serializer.data})
#     except Flat.DoesNotExist:
#         return HttpResponse("Invalid building no")
#     except:
#         return HttpResponse("something went wrong")

@csrf_exempt
def addadmin(request):
    if(request.method == "POST"):
        mydata = JSONParser().parse(request)
        admin_serialize = AdminSerializer(data=mydata)

        if (admin_serialize.is_valid()):
            admin_serialize.save()

            return JsonResponse(admin_serialize.data, status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization", status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get")

@csrf_exempt
def admin_all(request):
    if(request.method=="GET"):
        k=Admin.objects.all()
        admin_serializer=AdminSerializer(k,many=True)
        return JsonResponse(admin_serializer.data,safe=False)




@csrf_exempt
def addprepaid(request):
    if (request.method=="POST"):
      

        # mydata=JSONParser().parse(request)
        # prepaid_serialize=PrepaidSerializer(data=mydata)
        prepaid_serialize =PrepaidSerializer(data = request.POST)
        
        if (prepaid_serialize.is_valid()):
            prepaid_serialize.save()
            #return redirect(adminviewss)
            return JsonResponse(prepaid_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def addpostpaid(request):
    if (request.method=="POST"):
        # mydata=JSONParser().parse(request)
        postpaid_serialize=PostpaidSerializer(data=request.POST)
        
        if (postpaid_serialize.is_valid()):
            postpaid_serialize.save()
            #return redirect(adminviewss)
            return JsonResponse(postpaid_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)

@csrf_exempt
def adddongle(request):
    if (request.method=="POST"):
       

        # mydata=JSONParser().parse(request)
        dongle_serialize=DongleSerializer(data=request.POST)
        
        if (dongle_serialize.is_valid()):
            dongle_serialize.save()
            #return redirect(adminviewss)
            return JsonResponse(dongle_serialize.data,status=status.HTTP_200_OK)
        else:
            return HttpResponse("error in serialization",status=status.HTTP_400_BAD_REQUEST)
    else:
        return HttpResponse("no get",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def prepaid_all(request):
    if(request.method=="GET"):
        k=Prepaid.objects.all()
        prepaid_serializer=PrepaidSerializer(k,many=True)
        return JsonResponse(prepaid_serializer.data,safe=False)

@csrf_exempt
def postpaid_all(request):
    if(request.method=="GET"):
        k=Postpaid.objects.all()
        postpaid_serializer=PostpaidSerializer(k,many=True)
        return JsonResponse(postpaid_serializer.data,safe=False)

@csrf_exempt
def dongle_all(request):
    if(request.method=="GET"):
        k=Dongle.objects.all()
        dongle_serializer=DongleSerializer(k,many=True)
        return JsonResponse(dongle_serializer.data,safe=False)
# @csrf_exempt
# def f_single(request,fetchid):
    
#     sh=Flat.objects.get(id=fetchid)

    
#     if(request.method=="GET"):
#         flat_serialize=FlatSerializer(sh)
#         return JsonResponse(flat_serialize.data,safe=False,status=status.HTTP_200_OK)
#     if(request.method=="DELETE"):
#         sh.delete()
#         return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
#     if(request.method=="PUT"):
#         mydata=JSONParser().parse(request)
#         flat_serialize=FlatSerializer(sh,data=mydata)

#         if(flat_serialize.is_valid()):
#             flat_serialize.save()
#             return JsonResponse(flat_serialize.data,status=status.HTTP_200_OK)
#         else:
#             return JsonResponse(flat_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

#########query update#########################################################

@csrf_exempt
def viewquery(request):
    if (request.method=='GET'):
        query=Queries.objects.all()
        queryserial=QueriesSerializer(query,many=True)
        return response.JsonResponse(queryserial.data, safe=False)

def queryview(request):
    fetch=requests.get("http://127.0.0.1:8000/VoizFonica/viewquery/").json()
    return render(request,'viewqueries.html',{"data":fetch})

@csrf_exempt
def updatesearchapiquery(request):
    try:
        getid=request.POST.get("mobno")
        geti=Queries.objects.filter(mobno=getid)
        q_serializer=QueriesSerializer(geti,many=True)

        return render(request,"updatequery.html",{"data":q_serializer.data})
    except Queries.DoesNotExist:
        return HttpResponse("Invalid query")
    except:
        return HttpResponse("something went wrong")



@csrf_exempt
def update_data_readquery(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getmobno=request.POST.get('newmobno')
        getqueryname=request.POST.get('newqueryname')
        getquerydes=request.POST.get('newquerydes')
        getquerysolution=request.POST.get('newquerysolution')
        
        
        mydata={"mobno":getmobno,"queryname":getqueryname,"querydes":getquerydes,"querysolution":getquerysolution}
        jsondata=json.dumps(mydata)
        ApiLink="http://localhost:8000/VoizFonica/upa/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")

def updatequery(request):
    return render(request,'updatequery.html')

@csrf_exempt
def viewquerydetails(request,fetchid):
    
    query=Queries.objects.get(id=fetchid)
    if (request.method=='GET'):
        queryserial=QueriesSerializer(query) 
        return HttpResponse.JsonResponse(queryserial.data,safe=False,status=status.HTTP_200_OK)
    if (request.method=='PUT'):
        mydata=JSONParser().parse(request)
        queryserial=QueriesSerializer(query,data=mydata)
        if (queryserial.is_valid()):
            queryserial.save()
            return HttpResponse.JsonResponse(queryserial.data,status=status.HTTP_200_OK)

########################################################################################




# @csrf_exempt
# def updatesearchapi1(request):
#     try:
#         getprename=request.POST.get("prename")
#         getpre=Prepaid.objects.filter(prename=getprename)
#         prepaid_serializer=PrepaidSerializer(getpre,many=True)

#         # return render(request,"update.html",{"data":prepaid_serializer.data})
#     except Prepaid.DoesNotExist:
#         return HttpResponse("Invalid prename")
#     except:
#         return HttpResponse("something went wrong")


# @csrf_exempt
# def updatesearchapi2(request):
#     try:
#         getpostname=request.POST.get("postname")
#         getpost=Prepaid.objects.filter(postname=getpostname)
#         postpaid_serializer=PostpaidSerializer(getpost,many=True)

#         # return render(request,"update.html",{"data":postpaid_serializer.data})
#     except Postpaid.DoesNotExist:
#         return HttpResponse("Invalid postname")
#     except:
#         return HttpResponse("something went wrong")

# @csrf_exempt
# def updatesearchapi3(request):
#     try:
#         getdongle=request.POST.get("planname")
#         getdo=Dongle.objects.filter(planname=getdongle)
#         dongle_serializer=DongleSerializer(getdo,many=True)

#         # return render(request,"update.html",{"data":dongle_serializer.data})
#     except Dongle.DoesNotExist:
#         return HttpResponse("Invalid dongle name")
#     except:
#         return HttpResponse("something went wrong")
# @csrf_exempt
# def update_data_read1(request):
#     if (request.method=="POST"):
#         getnewid=request.POST.get('newid')
#         getprename=request.POST.get('newprename')
#         getpreamount=request.POST.get('newpreamount')
#         getprevalidity=request.POST.get('newprevalidity')
        
#         getprebenefits=request.POST.get("newprebenefits")
#         getpreofferdiscount=request.POST.get("newpreofferdiscount")
#         mydata={"prename":getprename,"preamount":getpreamount,"prevalidity":getprevalidity,"prebenefits":getprebenefits,"preofferdiscount":getpreofferdiscount}
#         jsondata=json.dumps(mydata)
#         ApiLink="http://localhost:8000/VoizFonica/view1/" +getnewid
#         requests.put(ApiLink,data=jsondata)
#         return HttpResponse("data has be updates successfully")
# @csrf_exempt
# def update_data_read3(request):
#     if (request.method=="POST"):
#         getnewid=request.POST.get('newid')
#         getplanname=request.POST.get('newplanname')
#         getdongleamount=request.POST.get('newdongleamount')
#         getdongleofferdiscount=request.POST.get('newdongleofferdiscount')
#         mydata={"planname":getplanname,"dongleamount":getdongleamount,"dongleofferdiscount":getdongleofferdiscount}
#         jsondata=json.dumps(mydata)
#         ApiLink="http://localhost:8000/VoizFonica/view3/" +getnewid
#         requests.put(ApiLink,data=jsondata)
#         return HttpResponse("data has be updates successfully")



# @csrf_exempt
# def update_data_read2(request):
#     if (request.method=="POST"):
#         getnewid=request.POST.get('newid')
#         getpostname=request.POST.get('newpostname')
#         getpostamount=request.POST.get('newpostamount')
#         getpostvalidity=request.POST.get('newpostvalidity')
        
#         getpostbenefits=request.POST.get("newpostbenefits")
#         getpostofferdiscount=request.POST.get("newpostofferdiscount")
#         mydata={"postname":getpostname,"postamount":getpostamount,"postvalidity":getpostvalidity,"postbenefits":getpostbenefits,"postofferdiscount":getpostofferdiscount}
#         jsondata=json.dumps(mydata)
#         ApiLink="http://localhost:8000/VoizFonica/view2/" +getnewid
#         requests.put(ApiLink,data=jsondata)
#         return HttpResponse("data has be updates successfully")

# @csrf_exempt
# def deletesearchapi1(request):
#     try:
#         getprename=request.POST.get("prename")
#         getpre=Prepaid.objects.filter(prename=getprename)
#         pre_serializer=PrepaidSerializer(getpre,many=True)
#         return render(request,"deleteprepaid.html",{"data":pre_serializer.data})
#     except Prepaid.DoesNotExist:
#         return HttpResponse("Invalid prename")
#     except:
#         return HttpResponse("something went wrong")

# @csrf_exempt
# def deletesearchapi2(request):
#     try:
#         getpostname=request.POST.get("postname")
#         getpost=Postpaid.objects.filter(postname=getpostname)
#         postpaid_serializer=PostpaidSerializer(getpost,many=True)
#         return render(request,"deletepostpaid.html",{"data":postpaid_serializer.data})
#     except Postpaid.DoesNotExist:
#         return HttpResponse("Invalid postname")
#     except:
#         return HttpResponse("something went wrong")

# @csrf_exempt
# def deletesearchapi3(request):
#     try:
#         getplanname=request.POST.get("planname")
#         getplan=Dongle.objects.filter(planname=getplanname)
#         dongle_serializer=DongleSerializer(getplan,many=True)
#         return render(request,"deletedongle.html",{"data":dongle_serializer.data})
#     except Dongle.DoesNotExist:
#         return HttpResponse("Invalid Dongle ")
#     except:
#         return HttpResponse("something went wrong")


# @csrf_exempt
# def delete_data_read1(request):
#     if (request.method=="POST"):
#         getnewid=request.POST.get('newid')
#         ApiLink="http://localhost:8000/Admins/view1/" +getnewid
#         requests.delete(ApiLink)
#         return HttpResponse("data has be deleted successfully")
# @csrf_exempt
# def delete_data_read2(request):
#     if (request.method=="POST"):
#         getnewid=request.POST.get('newid')
#         ApiLink="http://localhost:8000/Admins/view2/" +getnewid
#         requests.delete(ApiLink)
#         return HttpResponse("data has be deleted successfully")
# @csrf_exempt
# def delete_data_read3(request):
#     if (request.method=="POST"):
#         getnewid=request.POST.get('newid')
#         ApiLink="http://localhost:8000/VoizFonica/view3/" +getnewid
#         requests.delete(ApiLink)
#         return HttpResponse("data has be deleted successfully")

@csrf_exempt
def login_check(request):
    username=request.POST.get("username")
    password=request.POST.get("password")
    getadmin=Admin.objects.filter(username=username,password=password)
    admin_serializer=AdminSerializer(getadmin,many=True)
    if(admin_serializer.data):
        for i in admin_serializer.data:
            x=i["adminname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'try.html',{"data":admin_serializer.data})

    else:
        return HttpResponse("Invalid Credentials")        
            

def customer(request):
    return render(request,'add.html')

def viewplans(request):
    return render(request,'viewplans.html')

def viewCustomers(request):
    fetch = requests.get("http://127.0.0.1:8000/VoizFonica/viewall/").json()

    return render(request,'views.html',{"data": fetch})


def updateCustomers(request):
    return render(request,'update.html')

def registersuccess(request):
    return render(request,'cusregistersuccess.html')

@csrf_exempt
def addCustomer(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        c_serializer = CustomerSerializer(data = request.POST)
        if(c_serializer.is_valid()):
            c_serializer.save()
            # return JsonResponse(c_serializer.data,status=status.HTTP_200_OK)
            return redirect(registersuccess)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")

@csrf_exempt
def viewAll(request):
    if(request.method == "GET"):
        user = Customer.objects.all()
        us_serializer = CustomerSerializer(user, many=True)
        return JsonResponse(us_serializer.data, safe=False)

@csrf_exempt
def update_search(request):
    try:
        getCname = request.POST.get("cname")
        getCustomer = Customer.objects.filter(cname = getCname )
        cus_serializer = CustomerSerializer(getCustomer, many=True)
        return render(request,'update.html',{"data":cus_serializer.data}) 
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_data(request):
    getnewid = request.POST.get("newid")
    getcname = request.POST.get("newcname")
    getaddress = request.POST.get("newaddress")
    getmobno = request.POST.get("newmobno")
    getemail = request.POST.get("newemail")
    getaadharno = request.POST.get("newaadharno")
    
    getpassword = request.POST.get("newpassword")
    
    mydata= {"cname":getcname,"address":getaddress,"mobno":getmobno,"email":getemail,"aadharno":getaadharno,"password":getpassword}
    jsondata = json.dumps(mydata)
    Apilink = "http://127.0.0.1:8000/VoizFonica/view/"+getnewid
    requests.put(Apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")  

@csrf_exempt
def f_single(request,fetchid):
    
    sh=Customer.objects.get(id=fetchid)

    
    if(request.method=="GET"):
        cust_serialize=CustomerSerializer(sh)
        return JsonResponse(cust_serialize.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        sh.delete()
        return HttpResponse("deleted",status=status.HTTP_204_NO_CONTENT)
    if(request.method=="PUT"):
        mydata=JSONParser().parse(request)
        cust_serialize=CustomerSerializer(sh,data=mydata)

        if(cust_serialize.is_valid()):
            cust_serialize.save()
            return JsonResponse(cust_serialize.data,status=status.HTTP_200_OK)
        else:
            return JsonResponse(cust_serialize.errors,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
def login_checkcustomer(request):
    mob=request.POST.get("mobno")
    password=request.POST.get("password")
    getcustomer=Customer.objects.filter(mobno=mob,password=password)
    customer_serializer=CustomerSerializer(getcustomer,many=True)
    if(customer_serializer.data):
        for i in customer_serializer.data:
            x=i["cname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'customerservices.html')
    else:
        return HttpResponse("Invalid Credentials")


# @csrf_exempt
# def login_checkcustomer(request):
#     if request.method=="POST":
#         mobilenumber=request.POST.get('mobno')
#         password=request.POST.get('password')
#         data=Customer.objects.filter(mobno=mobilenumber,password=password)
#         if data:
#             customerdata=CustomerSerializer(data,many=True)
#             customerdata=customerdata.data
#             customerdata=customerdata[0]
#             customerdata=customerdata['id']
#             request.session['customer']=customerdata
#             print(request.session['customer'])
#             return render(request,'customerservices.html')
#         else:
#             return render(request,'login.html')
#     return render(request,'login.html')

# @csrf_exempt
# def Index(request):
#     if request.session.has_key('customer'):
#         udetail=request.session['customer']
#         data=Customer.objects.filter(id=udetail)
#         return render(request,'index.html',{'data':data})
#     else:
#         return redirect(Login)
# @csrf_exempt
# def CustomerUpdate(request):
#     if request.session.has_key('customer'):
#         id1=request.POST.get('id')
#         print("ID1",id1)
#         details=Customer.objects.get(id=id1)
#         customerdata=CustomerSerializer(request.POST)
#         customerdetails=CustomerSerializer(details,data=customerdata.data)
#         if customerdetails.is_valid():
#             customerdetails.save()
#             return redirect(Index)
#         else:
#             return HttpResponse(customerdetails.errors)
#     else:
#         return redirect(Login)


def loginviewcustomer(request):
    return render(request,"customerlogin.html")     
    
def homepage(request):
    return render(request,"landing.html")
def customerservices(request):
    return render(request,'customerservices.html')

def customerfaq(request):
    return render(request,'customerFAQ.html')



################### for query ###############################################################
@csrf_exempt
def addquery(request):
    if(request.method == "POST"):
        # mydict = JSONParser().parse(request)
        c_serializer = QueriesSerializer(data = request.POST)
        if(c_serializer.is_valid()):
            c_serializer.save()
            # return JsonResponse(c_serializer.data,status=status.HTTP_200_OK)
            return redirect(cusquery)
        else:
            return HttpResponse("Error in Serialization")
    else:
        return HttpResponse("GET method not allowed")

@csrf_exempt
def viewquery(request):
    if(request.method == "GET"):
        query = Queries.objects.all()
        queries_serializer = QueriesSerializer(query, many=True)
        return JsonResponse(queries_serializer.data, safe=False)

@csrf_exempt
def update_search(request):
    try:
        getCname = request.POST.get("cname")
        getCustomer = Customer.objects.filter(cname = getCname )
        cus_serializer = CustomerSerializer(getCustomer, many=True)
        return render(request,'update.html',{"data":cus_serializer.data}) 
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)


@csrf_exempt
def update_dataquery(request):
    getnewid = request.POST.get("newid")
    getmobno = request.POST.get("newmobno")
    getqueryname= request.POST.get("newqueryname")
    getquerydes= request.POST.get("newquerydes")
    getquerysolution = request.POST.get("newquerysolution")
    
    mydata= {"mobno":getmobno,"queryname":getqueryname,"querydes":getquerydes,"querysolution":getquerysolution}
    jsondata = json.dumps(mydata)
    Apilink = "http://127.0.0.1:8000/VoizFonica/view/"+getnewid
    requests.put(Apilink,data = jsondata)
    return HttpResponse("Data Updated Successfully")  

def cusquery(request):
    return render(request,"Customerquery.html")

def custf(request):
    return render(request,"CustomerFAQ.html")


from django.core.files.storage import FileSystemStorage
def upload(request):
    if request.method=='POST':
        uploaded_file=request.FILES['document']
  
        fs = FileSystemStorage()
        fs.save(uploaded_file.name,uploaded_file)
    return render(request,'add.html')


@csrf_exempt
def viewprepaidplans(request):
    if(request.method == "GET"):
        prepl = Prepaid.objects.all()
        p_serializer = PrepaidSerializer(prepl, many=True)
        return JsonResponse(p_serializer.data, safe=False)


def viewpreplans(request):
    fetch = requests.get("http://127.0.0.1:8000/VoizFonica/prepaidplans/").json()

    return render(request,'viewplans.html',{"data": fetch})


@csrf_exempt
def viewpostpaidplans(request):
    if(request.method == "GET"):
        postpl = Postpaid.objects.all()
        post_serializer = PostpaidSerializer(postpl, many=True)
        return JsonResponse(post_serializer.data, safe=False)


def viewpostplans(request):
    fetch = requests.get("http://127.0.0.1:8000/VoizFonica/postpaidplans/").json()

    return render(request,'viewpostplans.html',{"postdata": fetch})




def prepaidinvoice(request):
    return render(request,'mobilerecharge.html')
@csrf_exempt
def successrec(request):
    return render(request,'success.html')





@csrf_exempt
def addprepaidinvoice(request):
    if(request.method=="POST"):
        prepaidserializer=PrepaidinvoiceSerializer(data=request.POST)
        if (prepaidserializer.is_valid()):
            prepaidserializer.save() 
            return redirect(successrec)
        else:
            return HttpResponse("error")
    else:
        return HttpResponse("error in serialization")
    

from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
@csrf_exempt
def venue_pdf(request):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    getid = request.POST.get("id")
    # preinvoice=Prepaidinvoice.objects.filter(id=10)
    preinvoice=[Prepaidinvoice.objects.latest('id')]
    # lines=[
    #     "this is the text inside pdf",
    #     "this is the text inside pdf",
    #     "this is the text inside pdf",
    # ]
    
    lines=[] 
    for pre in preinvoice:
        # lines.append(pre.mobno)
        # lines.append(pre.typeservices)
        # lines.append(pre.pname)
        # lines.append(pre.pamount)
        # lines.append(pre.paymentmethod)
        # lines.append(pre.curdate)
        # lines.append("**")
    # textob.textLine(Customer.cname)
        lines.append("******-VOIZFONICA TELECOMS-******")
        lines.append("***-YOUR TRANSACTIONS DETAILS : ****** ")
        lines.append(" ")
      
        lines.append(" ")
        lines.extend(["Date & Time :" +         "  "+pre.curdate])
        lines.extend(["Mobile No :" +          "  " +pre.mobno])
        lines.extend(["Types of services :" +          "  "+pre.typeservices])
        lines.extend(["Plan Name :" +       "  "+pre.pname])
        lines.extend(["Amount :Rs" +        "  "+pre.pamount])
        lines.extend(["Payment Method :" +"  "+pre.paymentmethod])
        lines.append("Thank You!")
        

        lines.append("########################################")
    for line in lines:
        textob.textLine(line)
    
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='invoice.pdf')

def try1(request):
    return render(request,'try.html')

def about(request):
    return render(request,'about.html')
def contact(request):
    return render(request,'contact.html')

def services(request):
    return render(request,'services.html')

def ourservices(request):
    return render(request,'ourservices.html') 


def edit(request):
    return render(request,'Edit_profile.html')

def viewbill(request):
    return render(request,'View-bill.html')


@csrf_exempt
def login_checkcustomer(request):
    mob=request.POST.get("mobno")
    password=request.POST.get("password")
    getcustomer=Customer.objects.filter(mobno=mob,password=password)
    customer_serializer=CustomerSerializer(getcustomer,many=True)
    if(customer_serializer.data):
        for i in customer_serializer.data:
            x=i["cname"]
            y=i["id"]
            print(x)
        request.session['uname']=x
        request.session['uid']=y
        return render(request,'customerservices.html')
    else:
        return HttpResponse("Invalid Credentials")



# @csrf_exempt
# def login_checkcustomer(request):
#     print(1)
#     if request.method=="POST":
#         username=request.POST.get('mobno')
#         password=request.POST.get('password')
#         data=Customer.objects.filter(mobno=username,password=password)
#         if data:
#             userdata=CustomerSerializer(data,many=True)
#             userdata=userdata.data
#             print(userdata)
#             userdata=userdata[0]
#             userdata=userdata['id']
#             request.session['mobno']=userdata
#             print(request.session['mobno'])
#             return redirect(customerservices)
#         else:
#             return render(request,'customerservices.html')
#     return render(request,'customerservices.html')

# @csrf_exempt
# def Index(request):
#     if request.session.has_key('mobno'):
#         udetail=request.session['mobno']
#         data=Customer.objects.filter(id=udetail)
#         return render(request,'customerservices.html',{'data':data})
#     else:
#         return redirect(login)
# @csrf_exempt
# def Update(request):
#     if request.session.has_key('mobno'):
#         id1=request.POST.get('id')
#         print("ID1",id1)
#         details=Customer.objects.get(id=id1)
#         userdata=CustomerSerializer(request.POST)
#         userdetails=CustomerSerializer(details,data=userdata.data)
#         if userdetails.is_valid():
#             userdetails.save()
#             return redirect(customerservices)
#         else:
#             return HttpResponse(userdetails.errors)
#     else:
#         return redirect(customerservices)
# @csrf_exempt   
# def signout(request):
#     if request.session.has_key('mobno'):
#         del request.session['mobno']
#     return redirect(customerservices)


@csrf_exempt
def delete_cust(request):
    try:
        getFcode = request.POST.get("cname")
        getCode = Customer.objects.filter(cname = getFcode )
        fact_serializer = CustomerSerializer(getCode,many=True)
        return render(request,'customerdelete.html',{"data":fact_serializer.data})
        
    except:
        return HttpResponse("No Customer found",status=status.HTTP_404_NOT_FOUND)
    
   

@csrf_exempt
def delete_data(request):
    getnewid = request.POST.get("newid")
    apilink = "http://127.0.0.1:8000/VoizFonica/deletecust/"+getnewid
    requests.delete(apilink)
    return HttpResponse("Data deleted Successfully")


def viewCustomers(request):
    fetch = requests.get("http://127.0.0.1:8000/VoizFonica/viewall/").json()

    return render(request,'views.html',{"cusdata": fetch})


@csrf_exempt
def viewCust(request):
    if(request.method == "GET"):
        user = Customer.objects.all()
        us_serializer = CustomerSerializer(user, many=True)
        return JsonResponse(us_serializer.data, safe=False)

def manageCustomers(request):
    return render(request,'manageCustomers.html')


# def deleteCustomer(request, id):  
#     customer = Customer.objects.get(id=id)  
#     customer.delete() 
#     return redirect("http://127.0.0.1:8000/VoizFonica/viewall/")  






def cuslogout(request):
        logout(request)
        template='customerlogin.html'
        return render(request,template) 

def adminlogout(request):
        logout(request)
        template='login.html'
        return render(request,template)
    
@csrf_exempt
def prepaid_details(request, id):
    try:
        prepaids=Prepaid.objects.get(id=id)
    except Prepaid.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        prepaid_serializer=PrepaidSerializer(prepaids)
        return JsonResponse(prepaid_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        prepaids.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        prepaid_serialize=PrepaidSerializer(prepaids,data=mydict)
        if (prepaid_serialize.is_valid()):
            prepaid_serialize.save()
            return JsonResponse(prepaid_serialize.data,status=status.HTTP_200_OK)
        

#postpaid
@csrf_exempt
def postpaid_details(request, id):
    try:
        postpaids=Postpaid.objects.get(id=id)
    except Postpaid.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        postpaid_serializer=PostpaidSerializer(postpaids)
        return JsonResponse(postpaid_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        postpaids.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        postpaid_serialize=PostpaidSerializer(postpaids,data=mydict)
        if (postpaid_serialize.is_valid()):
            postpaid_serialize.save()
            return JsonResponse(postpaid_serialize.data,status=status.HTTP_200_OK)

#dongle
@csrf_exempt
def dongle_details(request, id):
    try:
        dongles=Dongle.objects.get(id=id)
    except Dongle.DoesNotExist:
        return HttpResponse("Invalid id",status=status.HTTP_404_NOT_FOUND)
    if(request.method=="GET"):
        dongle_serializer=DongleSerializer(dongles)
        return JsonResponse(dongle_serializer.data,safe=False,status=status.HTTP_200_OK)
    if(request.method=="DELETE"):
        dongles.delete()
        return HttpResponse("Deleted",status=status.HTTP_204_NO_CONTENT)    
    if(request.method=="PUT"):
        mydict=JSONParser().parse(request)
        dongle_serialize=DongleSerializer(dongles,data=mydict)
        if (dongle_serialize.is_valid()):
            dongle_serialize.save()
            return JsonResponse(dongle_serialize.data,status=status.HTTP_200_OK)





@csrf_exempt
def updatesearchapi1(request):
    try:
        getprename=request.POST.get("prename")
        getpre=Prepaid.objects.filter(prename=getprename)
        prepaid_serializer=PrepaidSerializer(getpre,many=True)

        return render(request,"updateprepaid.html",{"data":prepaid_serializer.data})
    except Prepaid.DoesNotExist:
        return HttpResponse("Invalid prename")
    except:
        return HttpResponse("something went wrong")


@csrf_exempt
def updatesearchapi2(request):
    try:
        getpostname=request.POST.get("postname")
        getpost=Postpaid.objects.filter(postname=getpostname)
        postpaid_serializer=PostpaidSerializer(getpost,many=True)

        return render(request,"updatepostpaid.html",{"data":postpaid_serializer.data})
    except Postpaid.DoesNotExist:
        return HttpResponse("Invalid postname")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def updatesearchapi3(request):
    try:
        getdongle=request.POST.get("planname")
        getdo=Dongle.objects.filter(planname=getdongle)
        dongle_serializer=DongleSerializer(getdo,many=True)

        return render(request,"updatedongle.html",{"data":dongle_serializer.data})
    except Dongle.DoesNotExist:
        return HttpResponse("Invalid dongle name")
    except:
        return HttpResponse("something went wrong")

@csrf_exempt
def update_data_read1(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getprename=request.POST.get('newprename')
        getpreamount=request.POST.get('newpreamount')
        getprevalidity=request.POST.get('newprevalidity')
        
        getprebenefits=request.POST.get("newprebenefits")
        getpreofferdiscount=request.POST.get("newpreofferdiscount")
        mydata={"id":getnewid,"prename":getprename,"preamount":getpreamount,"prevalidity":getprevalidity,"prebenefits":getprebenefits,"preofferdiscount":getpreofferdiscount}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://localhost:8000/VoizFonica/view1/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")
@csrf_exempt
def update_data_read3(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getplanname=request.POST.get('newplanname')
        getdongleamount=request.POST.get('newdongleamount')
        getvalidity=request.POST.get('newdonglevalidity')
        getdongleofferdiscount=request.POST.get('newdongleofferdiscount')
        gettypeofservices=request.POST.get('newtypeofservices')
        getdonglebenefits=request.POST.get('newdonglebenefits')
        mydata={"id":getnewid,"planname":getplanname,"dongleamount":getdongleamount,"donglevalidity":getvalidity,"dongleofferdiscount":getdongleofferdiscount,"typeofservices":gettypeofservices,"donglebenefits":getdonglebenefits}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://localhost:8000/VoizFonica/view3/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")



@csrf_exempt
def update_data_read2(request):
    if (request.method=="POST"):
        getnewid=request.POST.get('newid')
        getpostname=request.POST.get('newpostname')
        getpostamount=request.POST.get('newpostamount')
        getpostvalidity=request.POST.get('newpostvalidity')
        
        getpostbenefits=request.POST.get("newpostbenefits")
        getpostofferdiscount=request.POST.get("newpostofferdiscount")
        mydata={"id":getnewid,"postname":getpostname,"postamount":getpostamount,"postvalidity":getpostvalidity,"postbenefits":getpostbenefits,"postofferdiscount":getpostofferdiscount}
        jsondata=json.dumps(mydata)
        print(jsondata)
        ApiLink="http://localhost:8000/VoizFonica/view2/" +getnewid
        requests.put(ApiLink,data=jsondata)
        return HttpResponse("data has be updates successfully")


def bill(request):
    total=''
    if request.method=='POST':
        us=eval(request.POST.get('usage'))
        rat=eval(request.POST.get('rates'))
        extracl=eval(request.POST.get('extracall'))
        extracsmsc=eval(request.POST.get('extrasms'))
        extradatac=eval(request.POST.get('extradata'))
        total=(us*rat)+extracsmsc+extradatac+extracl
    return render(request,'bill.html',{'total':total})


@csrf_exempt
def viewdonplans(request):
    if(request.method == "GET"):
        prepl = Dongle.objects.all()
        p_serializer = DongleSerializer(prepl, many=True)
        return JsonResponse(p_serializer.data, safe=False)


def viewdongleplans(request):
    fetch = requests.get("http://127.0.0.1:8000/VoizFonica/d/").json()

    return render(request,'viewdongleplan.html',{"dondata": fetch})

# def viedongle(request):
#     return render(request,'viewdongleplan.html')

###################################bill############################################
from VoizFonica.models import Bill, Usage
from VoizFonica.serializers import BillSerializer, UsageSerializer
###################### adding usage functions#######
def addata(request):
    return render(request,"addusage.html")
@csrf_exempt
def addusagedata(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        usage_serialize=UsageSerializer(data=request.POST)
        if (usage_serialize.is_valid()):
            usage_serialize.save()
            #return redirect(viewall)
            return JsonResponse(usage_serialize.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)
###################################################################

def searchUsage(request):
    return render(request,'CUSTOMERsearch.html')
def searchadminUsage(request):
    return render(request,'ADMINsearch.html')
##########################################################################
####################seacrh api for customer
@csrf_exempt
def searchapi(request):
    try:
        getnewmob=request.POST.get("mobile")
        getusgae=Bill.objects.filter(mobile=getnewmob)
        usageserial=BillSerializer(getusgae,many=True)
        return render(request,"View-bill.html",{"data":usageserial.data})
    except Usage.DoesNotExist:
        return HttpResponse("invalid mobile")
    except:
        return HttpResponse("not runned")
##############################search api for admin
@csrf_exempt
def searchapi2(request):
    try:
        getnewmob=request.POST.get("mobile")
        getusgae=Bill.objects.filter(mobile=getnewmob)
        usageserial=BillSerializer(getusgae,many=True)
        return render(request,"ADMINsearch.html",{"data":usageserial.data})
    except Usage.DoesNotExist:
        return HttpResponse("invalid mobile")
    except:
        return HttpResponse("not runned")


#########################################################################
@csrf_exempt
def viewbillpost(request):
    if (request.method=='GET'):
        usage=Bill.objects.all()
        Usageserial=BillSerializer(usage,many=True)
        return response.JsonResponse(Usageserial.data, safe=False)

def billview(request):
    fetch=requests.get("http://127.0.0.1:8000/VoizFonica/viewbill/").json()
    return render(request,'adminviewbill.html',{"data":fetch})
#######################################################


from django.http import FileResponse
import io
from reportlab.pdfgen import canvas
from reportlab.lib.units import inch
from reportlab.lib.pagesizes import letter
@csrf_exempt
def billvenue_pdf(request,mobile):
    buf=io.BytesIO()
    c=canvas.Canvas(buf,pagesize=letter,bottomup=0)
    textob=c.beginText()
    textob.setTextOrigin(inch,inch)
    textob.setFont("Helvetica",14)
    usage=Usage.objects.filter(mobilen=mobile)
  
  
    lines=[] 
    for i in usage:
        lines.append('##############-VOIZFONICA TELECOMS-####################')
        lines.append('**************Your Transactions Details****************')
        lines.append(' ')
        lines.append('Usages')
       
        lines.extend(['YOUR MOBILE NUMBER :'+" "+i.mobilen])
        lines.extend(['CURRENT PLAN :'+" "+i.curplan])
        lines.extend(['EXTRA CALL  :'+" "+i.extracall])
        lines.extend(['EXTRA SMS  :'+" "+i.extrasms])
        lines.extend(['EXTRA DATA  :'+" "+i.extradata])
        
       
        lines.append("****************")

    for line in lines:
        textob.textLine(line)



    bill=Bill.objects.filter(mobile=mobile)
  
  
    billing=[] 
    for a in bill:
        
        billing.append(' ')
        billing.append('Charges ')
       
        billing.extend(['CURRENT DATE :'+" "+a.currdate])
        billing.extend(['CURRENT PLAN :Rs'+" "+a.curplancharge])
        billing.extend(['EXTRA CALL CHARGES :Rs'+" "+a.extracallcharge])
        billing.extend(['EXTRA SMS CHARGE :Rs'+" "+a.extrasmscharge])
        billing.extend(['EXTRA DATA CHARGE :Rs'+" "+a.extradatacharges])
        billing.extend(['TOTAL AMOUNT :Rs'+" "+a.totalamount])
       
        billing.append("****************")

    for b in billing:
        textob.textLine(b)
    c.drawText(textob)
    c.showPage()
    c.save()
    buf.seek(0)

    return FileResponse(buf,as_attachment=True,filename='second.pdf')
######################################## add bill data#################
@csrf_exempt
def addbilldata(request):
    if(request.method=="POST"):
        #mydict=JSONParser().parse(request)
        billserial=BillSerializer(data=request.POST)
        if (billserial.is_valid()):
            billserial.save()
            #return redirect(viewall)
            return JsonResponse(billserial.data,status=status.HTTP_200_OK)
        
        else:
            return HttpResponse("Error in serialization",status=status.HTTP_400_BAD_REQUEST)
      
    else:
        return HttpResponse("no get method allowed",status=status.HTTP_404_NOT_FOUND)

def addbill(request):
    return render(request,"addbill.html")

def billheader(request):
    return render(request,'billheader.html')

def Raisequery(request):
    return render(request,'Raisequery.html')

def querysolution(request):
    return render(request,'querysolution.html')

def viewquerysolution(request):
    fetch=requests.get("http://127.0.0.1:8000/VoizFonica/viewquery/").json()
    return render(request,'querysolution.html',{"data":fetch})

@csrf_exempt
def searchapis(request):
    try:
        getUsername = request.POST.get("mobno")
        getUser = Queries.objects.filter(mobno = getUsername )
        u_serializer =QueriesSerializer(getUser, many=True)
        return render(request,'querysolution.html',{"data":u_serializer.data})
        # return JsonResponse(u_serializer.data,safe=False,status=status.HTTP_200_OK)
        
    except:
        return HttpResponse("User not found",status=status.HTTP_404_NOT_FOUND)

def manage(request):
    return render(request,'manage.html')

############################SEND MAIL##########################
@csrf_exempt
def send_emailasfile(request):
    message=request.POST.get('message','')
    subject=request.POST.get('subject','')
    mail_id=request.POST.get('email','')
    email=EmailMessage(subject,message,EMAIL_HOST_USER,[mail_id])
    email.content_subtype='html'

    file =request.FILES['file']
    email.attach(file.name,file.read(),file.content_type)

    email.send()
    return HttpResponse("sent")

def customeremail(request):
    return render(request,'email.html')





