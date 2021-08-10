import csv,re,logging
import time
from datetime import date
logging.basicConfig(filename='medicines.log',level=logging.DEBUG)
medlist=[]
Header = ["rno","medname","price","mfgdate","expdate","type","uses","added_time"]
class medDetails:
    def addMedicine(self,rno,medname,price,mfgdate,expdate,type,uses,added_time):
        
        dict2={"rno":rno,"medname":medname,"price":price,"mfgdate":mfgdate,"expdate":expdate,"type":type,"uses":uses,"added_time":added_time}
        medlist.append(dict2)



def med_val(medname,price):
    val1=re.match("([A-Z]+)([a-z]+)([a-z]+)$",medname)
    val2=re.match("^[0-9]",price)
    if val1 and val2:
        return True
    else:
        return False

obj1=medDetails()          
      

try:

    while(True):
        print("1. Add Medicine details ")
        print("2. view all medicines ")
        print("3. Search for a medicine using type")
        print("4. Check the expiry date of medicines by date")
        print("5. Creating CSV files of medicine details")
        print("6. Exit")
        try:
            choice=int(input("Enter your choice:"))
        except ValueError:
            logging.error("User pressed wrong input")

        if choice==1:
            while(True):    
                medname=input("Enter the medicine name: ")
                price=input("Enter the cost of medicine: ")
                if med_val(medname,price):
                    rno=input("Enter the rack number: ")
                    mfgdate=input("Enter mfg date: ")
                    expdate=input("Enter expiry date: ")
                    type=input("Enter type of medicine: ")
                    uses=input("Enter usage and dosage of medicine: ")   
                    added_time =time.strftime("%H:%M:%S",time.localtime())  
                    obj1.addMedicine(rno,medname,price,mfgdate,expdate,type,uses,added_time)
                else:
                    print("Please entered valid name and cost")
                    continue
                break
                            
        if choice==2:
            print(medlist)
        if choice==3:
            search=input("Enter name to search for medicine")
            print(list(filter(lambda x:x["type"]==search,medlist)))
        if choice==4:
            today=date.today()
            a=today.strftime("%d/%m/%Y")
            print(list(filter(lambda i:i["expdate"]==str(a),medlist)))
        if choice == 5:
            with open("medDetails.csv", 'w+', encoding='UTF8', newline="") as b:
                writer = csv.DictWriter(b, fieldnames=Header)
                writer.writeheader()
                writer.writerows(medlist)
        if choice == 6:
            break   

except Exception:
    print("Something went wrong,Please try again")
    logging.error("Entered Inavlid data")
finally:
    print("Thank you!!!")    

                              
      


        
