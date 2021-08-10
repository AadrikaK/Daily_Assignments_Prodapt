
import time
import csv,logging,smtplib
from validation import validation_of_Patients
logging.basicConfig(filename='error1.log',level=logging.ERROR)

headercontent=["Serial number","Patinet's Name" ,"Patinet's Age:","Patinet's Sex (Male/Female)","Patinet's Height:","Patinet's Weight(In Kgs)","Patient's Blood Group:","Fathers Name:","Address:","City:","Phone number:","E-Mail:","Doctor's Name:", "Disease Name:","Bill Amount: Rs.","added"]

hospitallist=[]
class Hospital:
    def _init_(self):
        self.sno=0
        self.name=' '
        self.age=0
        self.sex=""
        self.email=" "
        self.fname=" "
        self.address=''
        self.city=''

        self.height=0
        self.weight=0
        self.doctor=''
        
        self.bill=0

        self.pno=0
        self.bgroup=''
        self.dname=''

    def Input(self):
        while(True):
            self.sno=input("Enter Serial number:")
            self.name=input("Enter Patinet's Name:")
            self.age=input("Enter Patinet's Age:")
            self.sex=input("Enter Patinet's Sex (Male/Female):")
            self.height=input("Enter Patinet's Height:")
            self.weight=input("Enter Patinet's Weight(In Kgs):")
            self.bgroup=input("Enter Patient's Blood Group:")
            self.fname=input("Enter Fathers Name:")
            self.address=input("Enter Address:")
            self.city=input("Enter City:")
            self.pno=input("Enter Phone number:")
            self.email=input("Enter E-Mail:")
            self.doctor=input("Enter Doctor's Name:")
            self.dname=input("Enter Disease Name:")
            self.bill=input("Enter Bill Amount: Rs.")
            if validation_of_Patients(self.sno ,self.name ,self.pno, self.email):
        
                current_local_time=time.strftime("%H:%M:%S",time.localtime())
                dict1={"Serial number":self.sno,"Patinet's Name":self.name ,"Patinet's Age:":self.age,"Patinet's Sex (Male/Female)":self.sex,"Patinet's Height:":self.height,"Patinet's Weight(In Kgs)":self.weight,"Patient's Blood Group:":self.bgroup,"Fathers Name:":self.fname,"Address:":self.address,"City:":self.city,"Phone number:":self.pno,"E-Mail:":self.email,"Doctor's Name:":self.doctor, "Disease Name:":self.dname,"Bill Amount: Rs.":self.bill,"added":current_local_time}
                hospitallist.append(dict1)
                return hospitallist
            else:
                print("enter valid information ")
                continue
            break
       
    def Output(self):
        print ("SERIAL NUMBER:-",self.sno)
        print ("PATIENT'S NAME:-",self.name)
        print ("PATIENT'S AGE:-",self.age)
        print ("PATIENT'S SEX:-",self.sex)
        print ("PATIENT'S HEIGHT:-",self.height)
        print ("PATIENT'S WEIGHT:-",self.weight)
        print ("PATIENT'S BLOOD GROUP:-",self.bgroup)
        print ("FATHERS NAME:-",self.fname)
        print ("ADDRESS:-",self.address)
        print ("CITY:-",self.city)
        print ("CONTACT NUMBER:-",self.pno)
        print ("E-MAIL ADDRESS:-",self.email)
        print ("DISEASE NAME:-",self.dname)
        print ("DOCTOR'S NAME:-",self.doctor)
        print ("BILL AMOUNT:-",self.bill)




def WriteHospital():
    
    ob=Hospital()
    # ob.Input()
    records=ob.Input()

    with open("hospital.csv","w+",encoding="UTF8",newline="") as s:
            writer=csv.DictWriter(s,fieldnames=headercontent)
            writer.writeheader()
            writer.writerows(records)


    print("record saved")

    print("your details are")
    ob.Output()
    
  
def ReadHospital():
    
    ob=Hospital()
     
    with open("hospital.csv","r",encoding="utf-8") as f:
        read=csv.DictReader(f)
        for d in read:
            print("\n")
            print(d)

            
def mailing(n) :
            with open("hospital.csv","r",encoding="utf-8") as f:
                read=csv.DictReader(f)
                for d in read:
                    if d["Serial number"]==n:
                        cost=d["'Bill Amount: Rs."]
            message=cost
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("ridhimathur10@gmail.com","ridhima@10")
            connection.sendmail("ridhimathur10@gmail.com",Hospital.email,message)
            logging.info("Mail sent")
            print("Sending email")  
    