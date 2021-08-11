import datetime,time,csv,re,logging,pymongo
productlist=[]
try:
    
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['productDb'] #database
    collection_name=mydatabase['product']
    class ProductDetails:
        def init(self,pname,pcode,dname,manufacturingyear,reatilprice,wholesaleprice,pdescription,mphno):
            self.pname=pname
            self.pcode=pcode
            self.dname=dname
            self.manufacturingyear=manufacturingyear
            self.reatilprice=reatilprice
            self.wholesaleprice=wholesaleprice
            self.pdescription=pdescription  
            self.mphno=mphno  
        def addproductdetail(self,pname,pcode,dname,manufacturingyear,reatilprice,wholesaleprice,pdescription,mphno):
        
            dict1={"pname":pname,"pcode":pcode,"dname":dname,"manufacturingyear":manufacturingyear,"retailprice":reatilprice,"wholesaleprice":wholesaleprice,"pdescription":pdescription,"mphno":mphno} 
            print(dict1)  
            return dict1  
    def validate(pname,pdescription,dname):
        valpname=re.search("[A-Z]{1}[^A-Z]{0,25}$",pname)
        valpdescription=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",pdescription)
        valdname=re.search("[A-Z]{1}[^A-Za-z]{0,100}$",dname)
        
        if valpname and valpdescription and valdname:
            return True
        else:
            return False 
    obj=ProductDetails()    
    while True:
        print("1.Add Product")
        print("2.View products")
        print("3.Search a product")
        print("4.Delete a product")
        print("5.Update product details")
        print("6.Exit")
        choice=int(input("Enter your choice : "))

        if choice==1:
            pname=input("Enter the Product name : ")
            pcode=input("Enter the product code : ")
            dname=input("Enter the Distributor name : ")
            manufacturingyear=input("Enter the manufacturer year : ")
            retailprice=input("Enter the retail price : ")
            wholesaleprice=input("Enter the wholesale price : ")
            pdescription=input("Enter the product description : ")
            mphno=input("Enter the manufacturer ph no : ")
            if validate(pname,pdescription,dname)==True:
                
                data=obj.addproductdetail(pname,pcode,dname,manufacturingyear,retailprice,wholesaleprice,pdescription,mphno)
                productlist.append(data)
                result=collection_name.insert_many(productlist)
                print(result.inserted_ids)    
        if choice==2:
            result= collection_name.find({},{"_id":0}) 
            productlist=[]
            for i in result:
                productlist.append(i)
            print(productlist)
        if choice==3:
            sea=input("Enter the P code :")
            result= collection_name.find({"pcode":sea},{"_id":0}) 
            for j in result:
                print(j)
        
        if choice==4:
            de=input("Enter the pcode :")
            result= collection_name.delete_many({"pcode":de}) 
            print(result) 
        if choice==5:
            s=input("Enter the pcode :")
            t=input("Enter the retailprice to be updated")
            result= collection_name.update_one({"pcode":s},{"$set":{"retailprice":t}})
            print(result)
        if choice==6:
            break         
except:
    logging.error("Error")  
finally:
    print("Thank you")          