import json,smtplib,re,logging,time
clist=[]
class Customer:
    def addCustomer(self,name,mobileNumber,emailId,dish1,dish2,dish3,dish4,dish5,num1,num2,num3,num4,num5):
        current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
        dict1={"name":name,"mobileNumber":mobileNumber,"emailId":emailId,"dish1":dish1,"dish2":dish2,"dish3":dish3,"dish4":dish4,"dish5":dish5,"num1":num1,"num2":num2,"num3":num3,"num4":num4,"num5":num5,"AddOn":current_time}
        clist.append(dict1)
k=Customer()
def validate(name,mobileNumber,emailId):
        name1=re.search("[A-Za-z]{0,25}$",name)
        print(name1)
        mobileNumber1=re.search("^(\+91)[6-9]\d{9}$",mobileNumber)
        print(mobileNumber1)
        emailId1=re.search( "[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",emailId)
        print(emailId1)   
        if name1 and  mobileNumber1 and emailId1:
            return True
        else:
            return False  
try:
    if __name__=="__main__":            
        while(True):
            print("1.Add Customer")
            print("2. view Customer")
            print("3.View all Customer details using JSON File")
            print("4.Send an email to all customer")
            print("5.Search customer based on name")
            print("6.Exit")
            choice=int(input("Enter your choice :"))
            if choice==1:
                name = input("Enter the name of Customer")
                mobileNumber=input("Enter the mobilenumber:")
                emailId=input("Enter the email:")
                if validate(name,mobileNumber,emailId):
                    dish1=input("Enter the dish1:")
                    dish2=input("Enter the dish2 :")
                    dish3=input("Enter the dish3 :")
                    dish4=input("Enter the dish4 :")
                    dish5=input("Enter the dish5 :")
                # while(1):
                #     print("1) Massla dosa")
                #     print("2) rice")
                #     print("3) chicken")
                #     print("4) roti")
                #     print("5) paneer")
                #     option=int(input(("enter a optin: ")))
                #     if option==1:
                #         print("please enter how many how many masala dosa u wnat to eat")
                #         num1 = int(input("Enter the number of dish1:"))
                #     if option==2
                #         print("please enter how many how many masala dosa u wnat to eat")
                    num1 = int(input("Enter the number of dish1: "))
                    num2 = int(input("Enter the number of dish2: "))
                    num3 = int(input("Enter the number of dish3: "))
                    num4= int(input("enter the number of dish4:"))
                    num5=int(input("enter the number of dish5:"))
                #if validate(name,mobileNumber,emailId):
                    k.addCustomer(name, mobileNumber, emailId, dish1, dish2, dish3, dish4, dish5,num1,num2,num3,num4,num5)
                else:

                    print("Please enter correct infomation ")
                    continue
                
            if choice==2:
                print(clist)
            if choice==3:
                jsondata=json.dumps(clist)
                with open("mcustomer.json","w+",encoding="utf-8") as c1:
                    c1.write(jsondata)

            if choice==4:
                cprod=input("Enter customer want  to search: ")
                print(list(filter(lambda i:i["name"]==cprod,clist)))
                jsondata=json.dumps(clist)
                with open("ncustomer.json","w+",encoding="utf-8") as s2:
                    s2.write(jsondata)

            if choice==5:
                for i in clist:
                    message1 =i["num1"]*20+i["num2"]*10+i["num3"]*50+i["num4"]*60+i["num5"]*70
                    message="Your total amount is " +str(message1)
                    print(message)
                    connection=smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("Arifkhanstar0786@gmail.com","Absrkhan078621")
                    connection.sendmail("Arifkhanstar0786@gmail.com",i["emailId"],message)
                    connection.quit
                    print("Mail sent successfully")

            if choice==6:
                break
except:
    logging.error("something went wrong")               

