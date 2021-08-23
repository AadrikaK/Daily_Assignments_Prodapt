import logging,pymongo,smtplib
from valid import validatemail, validation_of_passenger

passengers=[]
tickets=[]
bookedlist=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["Railwaydb"]
collection1=mydb["passengers"]
collection2=mydb["tickets"]

class Booking:
    def passengersdetails(self,passenger_id,passenger_name,gender,age,email,phone_no,from_station,to_station):
        dict1={"passenger_id":passenger_id,"passenger_name":passenger_name,"gender":gender,"age":age,"email":email,"phone_no":phone_no,"from_station":from_station,"to_station":to_station}
        passengers.append(dict1)
    
    def ticketsdetails(self,ticket_id,train_no,passenger_id,from_station,to_station):
        dict2={"ticket_id":ticket_id,"train_no":train_no,"passenger_id":passenger_id,"from_station":from_station,"to_station":to_station}
        tickets.append(dict2)
obj1=Booking()


def reservation():
    email=input("enter passenger email")
    
    if validatemail(email):
        while True:
            print("1.BOOK A TICKET")
            print("2.VIEW BOOKED TICKETS")
            print("3.CLOSE")
            try:
                choice=int(input("Enter your choice : "))
            except:
                logging.error("choice should be an integer")

            if choice==1:               
                passenger_id=int(input("Enter the passenger id : "))
                passenger_name=input("Enter the passenger name : ")
                gender=input("Enter the gender of the passenger: ")
                age=input("Enter the age of the passenger: ")
                email=input("Enter email-id: ")
                phone_no=int(input("Enter the passenger's mobile number: "))
                from_station=input("Enter the from station: ")
                to_station=input("Enter the to station: ")

                if validation_of_passenger(passenger_name,age,email,from_station,to_station):
                    obj1.passengersdetails(passenger_id,passenger_name,gender,age,email,phone_no,from_station,to_station)
                    result=collection1.insert_many(passengers)
                    print(result.inserted_ids) 
                
                else:
                    print("enter valid information ")
                    continue

                    
                ticket_id=int(input("Enter the ticket id : "))
                train_no=int(input("Enter the train number: "))
                passenger_id=int(input("Enter the passenger id : "))
                from_station=input("Enter the from station: ")
                to_station=input("Enter the destination station: ")

                obj1.ticketsdetails(ticket_id,train_no,passenger_id,from_station,to_station)
                result=collection2.insert_many(tickets)

                for i in tickets:
                    ticket_id=i["ticket_id"]
                print("your ticket has been booked successfully, check your mail for details")
                message="\n your ticket is booked."+"\n your ticket_id is :"+str(ticket_id)+"\n Thank you!! \n Have a safe journey"
                connection=smtplib.SMTP("smtp.gmail.com",587)
                connection.starttls()
                connection.login("sowmya070721@gmail.com","sowmya@0707")
                connection.sendmail("sowmya070721@gmail.com",email,message)
                print("Email sent successfully")
                connection.quit()
            
            if choice==2:
                result=collection2.find({},{"_id":0})
                for i in result:
                    bookedlist.append(i)
                    print(bookedlist)
                    bookedlist.clear()
                
            if choice==3:
                break
            else:
                logging.error("Enter a valid email")
        