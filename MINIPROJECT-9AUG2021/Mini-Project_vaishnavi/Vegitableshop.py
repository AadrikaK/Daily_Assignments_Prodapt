import smtplib,time,logging
import validate as vegi
try:
    print("*****@@@@@@ VEGITABLE SHOP @@@@@@*****")
    vegitable_list=[]
    class VegitableDetails:
        def addvegidetails(self,vegitable_name,price,packing_date,expiry_date):
            current_time=time.strftime("%m-%d-%Y %H:%M:%S",time.localtime())
            dict1={"vegitable_name":vegitable_name,"price":price,"packing_date":packing_date,"expirydate":expiry_date,'AddOn':current_time}
            vegitable_list.append(dict1)
    obj1=VegitableDetails()
    while(True):
        print("1.Add Vegitables :-")
        print("2.View all vegitables details :-")
        print("3.Customer Details :-")
        print("4.List all the vegitable that expired today :-")
        print("5.Search the vegitable by name :-")
        print("6.Exit :-")
        choice=int(input("enter your choice:"))
        if choice==1:
            vegitable_name=input("enter the vegitable name - ")
            price=input("enter the price of vegitable  - ")
            packing_date=input("enter vegitable manufacturing date in mm-dd-yyyy format - ")
            expiry_date=input("enter the expiry date in mm-dd-yyyy format - ")
            obj1.addvegidetails(vegitable_name,vegi.val_price(price),packing_date,expiry_date)
            
        elif(choice==2):
            print(vegitable_list) 
        elif(choice==3):
            name= input("enter your name :-")
            emailid = input('enter your emailid :-')
            total_vegitable = []
            final_total=0
            for i in vegitable_list:
                print('vegitable name - ',i['vegitable_name'] ,' price of vegitable - ',i['price'])
                x = int(input('enter the number of packet that you want (0 if you don\'t want)  -  '))
                total = i['price']*x
                final_total += total 
                if x > 0:
                    total_vegitable.append(i["vegitable_name"])
                    total_vegitable.append(i['price'])
                    total_vegitable.append(x)
            print('customer name - ',name)
            print('customer emailid - ',vegi.val_emailid(emailid))
            print(total_vegitable)
            print('your total amount is - ', final_total)
 
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("vaishnavi.p6521@gmail.com","Priy@6521")
            message='your total amount is - '+str(final_total)
            connection.sendmail("vaishnavi.p6521@gmail.com",emailid, message)
            print("Message sended successful")
            connection.quit()
             
        elif(choice == 4):
            print("list all the vegitables that expire today - ")
            current_date=time.strftime("%m-%d-%Y-",time.localtime())
            expired=(list(filter(lambda i:i["expirydate"]==str(current_date),vegitable_list)))    
            if len(expired)>0:
                print(expired)
            else:
                print("No Expired vegitable found")

        elif(choice == 5):
            I=input("enter the vegitable that you want to search - ")
            print(list(filter(lambda i:i["vegitablename"]==I,vegitable_list)))  

        elif(choice==6):
            break

except Exception:
    logging.error("Something went wrong")
else:
    print("Your program completed Successfully")
finally:
    print("Thank You!!")