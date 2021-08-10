import csv,json,re,logging
import getpass

try:
    username="kanchana"
    password="Kanchana@8+"
    headerContent=["dogName","dogId","dogAge","dogprice"]
    class DogDetails:
        def _init_(self,dogName,dogId,dogAge,dogPrice):
            self.dogName=''
            self.dogId=''
            self.dogAge=''
            self.dogPrice=''
       
        def adddogdetail(self,dogName,dogId,dogAge,dogPrice):
            dict1={"dogName":dogName,"dogId":dogId,"dogAge":dogAge,"dogprice":dogPrice}
            doglist.append(dict1)
            return dict1

    def validate(dogName): 
        valname=re.search("[A-Z]{1}[^A-Z]{0,25}$",dogName) 
        if valname:
            return True
        else:
            return False 
    obj=DogDetails()
    doglist=[]
    Price_list=[]
    Age_list=[]
    if(__name__=="__main__"):     
        user_name=input("please enter your username:")
        pass_word=getpass.getpass(prompt='Please enter your password:')
        if user_name==username and pass_word==password:
            while True:
                print("1.add dog details")
                print("2.view all dogs")
                print("3.search a dog by name")
                print("4.Sorting of dogs according to price")
                print("5 displaying the oldest dog")
                print("6.Generate csv file")
                print("7.To generate json file")
                print("8.exit") 
                choice=int(input("Enter your choice : "))
                
                if choice==1:
                    dogName=input("Enter the dogname : ")
                    dogId=int(input("Enter the dogId : "))
                    
                    dogAge=int(input("Enter the Age:"))
                    dogPrice=int(input("Enter the dog price:"))
                    a=validate(dogName)
                    if a:
                        obj.adddogdetail(dogName,dogId,dogAge,dogPrice)
                    else:
                        logging.error("invalid data enter a valid data")
                if choice==2:
                    print(json.dumps(doglist))
                if choice==3:
                    name=input("Enter the dogName to search : ")
                    print(list(filter(lambda i:i["dogName"]==name,doglist)))
                if choice==4:
                    Price_list=sorted(doglist,key=lambda i:i["dogprice"],reverse=True)
                    print(Price_list)
                if choice==5:
                    print("displaying the oldest dog")
                    Age_list=sorted(doglist,key=lambda i:i["dogAge"],reverse=True)
                    for i in Age_list:
                        print(i)
                        break
                if choice==6:
                    with open("dog.csv","w+",encoding="UTF8",newline='')as s:
                        writer=csv.DictWriter(s,fieldnames=headerContent)
                        writer.writeheader()
                        writer.writerows(doglist)
                if choice==7:
                    myjson=json.dumps(doglist) 
                    with open("dog.json","w+",encoding="utf-8")as s:
                        s.write(myjson)
                if choice==8:
                    break
        else:
            logging.error("username or password is incorrect please try again")
except:
    logging.error("unable to process")