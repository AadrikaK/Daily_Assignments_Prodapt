import re,collections,time,csv,logging,pymongo
empdict={}
try:
    client=pymongo.MongoClient("mongodb://localhost:27017/") #establishing connection
    mydatabase=client['employeeDb1'] #database
    collection_name=mydatabase['employeee']
    class emp:
        def addEmployee(self):
            name=input("Enter the name: ")
            designation=input("Enter the Designation: ")
            salary=input("Enter the salary :")
            address=input("Enter the address : ")
            pincode=input("Enter the pincode : ")
            dict1={"name":name,"designation":designation,"salary":salary,"address":address,"pincode":pincode}
            return dict1
    def validate(dict1):
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dict1["name"])
        valsalary=re.search("[0-9]{0,7}$",dict1["salary"])
        if valname and valsalary:
            return True
        else:
            return False
    obj=emp()
    while(1):
        print("1. Add employee")
        print("2. view employee")
        print("3. search employee by name")
        print("4. delete employee by name")
        print("5. Update employee ")
        print("6. Exit")
        option=int(input("Enter your option :"))
        if option==1:
            n=int(input("Enter the number of employees :"))
            for i in range(0,n):
                a=obj.addEmployee()
                if len(empdict)==0:
                    empdict=collections.ChainMap(a)
                    result=collection_name.insert_one(empdict)
                    print(result.inserted_id) 
                else:
                    empdict=empdict.new_child(a)      
        if option==3:
            sea=input("Enter the name :")
            result= collection_name.find({"name": sea},{"_id":0}) 
            
            for j in result:
                print(j)
        if option==2:
            result= collection_name.find({},{"_id":0})
            emplist=[]
            for i in result:
                emplist.append(i)
            print(emplist)
        if option==4:
            de=input("Enter the name :")
            result= collection_name.delete_many({"name":de}) 
            print(result) 
        if option==5:
            s=input("Enter the name :")
            t=input("Enter the salary to be updated")
            result= collection_name.update_one({"name":s},{"$set":{"salary":t}})
            print(result) 
        if option==6:
            break
           
except:
    logging.error("OOPS!! Something went wrong")
finally:
    print("Thank you")        