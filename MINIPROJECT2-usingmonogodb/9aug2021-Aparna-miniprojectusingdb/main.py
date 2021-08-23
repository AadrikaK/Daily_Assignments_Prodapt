import logging,pymongo,getpass
from valid import validation_of_traindetails
import reservation
logging.basicConfig(filename='error.log',level=logging.INFO)


trains=[]
fetchlist=[]
passengers=[]
tickets=[]
client=pymongo.MongoClient("mongodb://localhost:27017/")
mydb=client["Railwaydb"]
collection=mydb["trains"]


class TrainDetails:
    def addtrains(self,train_no,train_name,start_station,dest_station):
        dict1={"train_no":train_no,"train_name":train_name,"start_station":start_station,"dest_station":dest_station}
        trains.append(dict1)
obj=TrainDetails()

# class Reservation:
#     def passengers(self,passenger_id,passenger_name,gender,age,email,phone_no,from_station,to_station):
#         dict1={"passenger_id":passenger_id,"passenger_name":passenger_name,"gender":gender,"age":age,"email":email,"phone_no":phone_no,"from_station":from_station,"to_station":to_station}
#         passengers.append(dict1)
    
#     def tickets(self,ticket_id,train_no,passenger_id,from_station,to_station):
#         dict2={"ticket_id":ticket_id,"train_no":train_no,"passenger_id":passenger_id,"from_station":from_station,"to_station":to_station}
#         tickets.append(dict2)
    
    

username="aparna12"
password="appu@123"
user_name=input("please enter your username:")
pass_word=getpass.getpass(prompt='Please enter your password:')
if user_name==username and pass_word==password:
    while(True):
        print("------------------------------------")
        print("\n RAILWAY RESERVATION SYSTEM")
        print("\n------------------------------------")
        print("1.ADD TRAIN DETAILS")
        print("2.VIEW ALL TRAINS")
        print("3.SEARCH TRAIN BY NAME")
        print("4.DELETE TRAIN BY NAME")
        print("5.UPDATE TRAIN NAME BY ID")
        print("6.RESERVATION OF TICKETS")
        print("7.exit")
        try:
            choice=int(input("Enter your choice : "))
        except:
            logging.error("choice should be an integer")
        else:
            logging.info("Right choice")

        if choice==1:
            train_no=int(input("Enter the train number : "))
            train_name=input("Enter the train name : ")
            start_station=input("Enter the start station : ")
            dest_station=input("Enter the destination station : ")

            if validation_of_traindetails(train_name,start_station,dest_station):
                obj.addtrains(train_no,train_name,start_station,dest_station)
                result=collection.insert_many(trains)
                print(result.inserted_ids)
            else:
                print("enter valid information ")
                continue

        if choice==2:
            result=collection.find({},{"_id":0})
            for i in result:
                fetchlist.append(i)
                print(fetchlist)
                fetchlist.clear()

        if choice==3:
            name=input("Enter the train_name to search : ")
            result=collection.find({"train_name":name})
            for i in result:
                print(i)

        if choice==4:
            name=input("Enter the train name that has to be deleted:")
            result=collection.delete_many({"train_name":name})
            print(name," is deleted")

        if choice==5:
            train_no=int(input("Enter the train number to be updated:"))
            new_name=input("Enter the new name of the train:")
            result=collection.update_one({"train_no":train_no},{"$set":{"train_name":new_name}})
            print("Updated successfully")

        if choice==6:
            reservation.reservation()


        if choice==7:
            break
        

