import time,re
from datetime import datetime
import csv

header=['name','descrp','price','manuf','manudate','expiry']

productlist=[]

class productdetails:
    def addproducts(self,name,descrp,price,manuf,manudate,expiry):
        dict1={"name":name,"descrp":descrp,"price":price,"manuf":manuf,"manudate":manudate,"expiry":expiry}
        productlist.append(dict1)

obj1=productdetails()
while(1):
    print("1. add products: ")
    print("2. view all products :")
    print("3. search a product: ")
    print("4. list all products that expire today: ")
    print("5. save to fille product: ")
    print("6. exit:")
    
    option=int(input("enter choice"))

# try:
    if option==1:
        name=input("enter name: ")
        descrp=input("enter product description: ")
        price=int(input("enter the price: "))
        manuf=input("enter manufactures: ")
        manudate=input("enter manufacture date: ")
        expiry=input("enter expiry date: ")

        def val(name,descrp,price):
            vn=re.search("^[A-Z]?[a-z]",name)
            vd=re.search("^[A-Z]",descrp)
            vp=re.search("^[1-9]",price)
            if vn and vd and vp:
                return True
            else:
                return False
        obj1.addproducts(name,descrp,price,manuf,manudate,expiry)

    if option==2:
        print("list of all products: ")
        print(productlist)

    if option==3:
        print("search product: ")
        name=input("enter product name: ")
        print(list(filter(lambda i:i ["name"==proname,productlist])))

    if option==4:
        current=time.localtime()
        date=time.strftime("%Y- %m- %d",current)
        ex=(list(filter(lambda i:i["expiry"]==date,productlist)))
        print(productlist)
        
        if len(ex)>0:
            print(ex)

        else:
            print("no expiry products")

    if option==5:
        with open('product.csv','w+',encoding='UTF8',newline='') as p:
            writer=csv.DictWriter(p,fieldnames=header)
            writer.writeheader()
            writer.writerows(productlist)
# except exception:
#     print("going wrong")
# else:
#     print("done")
# finally:
#     print("completed")

    if option==6:
        break