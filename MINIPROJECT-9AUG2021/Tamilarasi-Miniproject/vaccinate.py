import smtplib,re,logging,json,time,csv
from datetime import date
try:
    headerContent=["name","age","mbl_no","mail_id","gender","address","proof_name","proof_no","slot_date","vaccine_count","vaccine_name","vaccinated_by","vaccinated_place"]
    vaccinatelist=[]
    logging.basicConfig(filename='vaccinate.log',level=logging.DEBUG)
    class Patient:
        def __init__(self,name,age,mbl_no,mail_id,gender,address,proof_name,proof_no,slot_date):
            self.name=name
            self.age=age
            self.mbl_no=mbl_no
            self.mail_id=mail_id
            self.gender=gender
            self.address=address
            self.proof_name=proof_name
            self.proof_no=proof_no
            self.slot_date=slot_date

    class resultPatient(Patient):
        def __init__(self,name,age,mbl_no,mail_id,gender,address,proof_name,proof_no,slot_date,vaccine_count,vaccine_name,vaccinated_by,vaccinated_place):
            super().__init__(name,age,mbl_no,mail_id,gender,address,proof_name,proof_no,slot_date)
            self.vaccine_count=vaccine_count
            self.vaccine_name=vaccine_name
            self.vaccinated_by=vaccinated_by
            self.vaccinated_place=vaccinated_place
            dict={"name":name,"age":age,"mbl_no":mbl_no,"mail_id":mail_id,"gender":gender,"address":address,"proof_name":proof_name,"proof_no":proof_no,"slot_date":slot_date,"vaccine_count":vaccine_count,"vaccine_name":vaccine_name,"vaccinated_by":vaccinated_by,"vaccinated_place":vaccinated_place}
            vaccinatelist.append(dict)

    def validate(vname,vmobile_number,vemail_id):
            name1=re.search("^[A-Z]{1}[a-z]{0,25}$",vname)
            print(name1)
            mobilenumber1=re.search("^91[6-9]\d{9}$",vmobile_number)
            print(mobilenumber1)
            emailid1=re.search("[A-Za-z0-9]{0,20}@[a-z]+\.[a-z]{2,4}$",vemail_id)
            print(emailid1)
            if name1 and mobilenumber1 and emailid1:
                return True
            else:
                return False

    if __name__== "__main__":
        while(1):
            print("1.Add Patient Details")
            print("2.View all the patient Details Using JSON")
            print("3.View the Patient Details Based on name")
            print("4.View the Today Vaccine Patient Details Using Slot Booking")
            print("5.Maintain all the Patiet Details in File")
            print("6.Send all Patient Details for Mail")
            print("7.Exit")
            option=int(input("Enter Your Option:"))
            if option==1:
                vname=input("Enter the Patient Name:")
                age=input("Enter the Patient Age:")
                vmobile_number=input("Enter the Patient Mobile Number:")
                vemail_id=input("Enter the Patient EmailId:")
                gender=input("Enter the Patient Gender:")
                address=input("Enter the Patient Address:")
                proof_name=input("Enter the Patient Proof Name:")
                proof_no=input("Enter the Patient Proof Number:")
                slot_date=input("Enter the Vaccinate Slot Date:")
                vaccine_count=input("Enter the Vaccinate Count:")
                vaccine_name=input("Enter the Vaccinate Name:")
                vaccinated_by=input("Enter the Vaccinate By:")
                vaccinated_place=input("Enter the Vaccinate Place:")
                if validate(vname,vmobile_number,vemail_id):
                    obj=resultPatient(vname,age,vmobile_number,vemail_id,gender,address,proof_name,proof_no,slot_date,vaccine_count,vaccine_name,vaccinated_by,vaccinated_place)
                    print(vaccinatelist)
                else:
                    logging.error("Wrong!Check Your Validation")

            if option==2:
                jsondata=json.dumps(vaccinatelist)
                with open('VaccinateList.json','w+',encoding="utf-8") as f1:
                    f1.write(jsondata)
                    logging.info("Successfully!!!!Save all the JSON File!!!! ")

            if option==3:
                sName=input("Ënter the Name to Search:")
                print(list(filter(lambda i:i["name"]==sName,vaccinatelist)))

            if option==4:
                current_time=time.localtime()
                tday=time.strftime("%d.%m.%Y",current_time)
                slot_date=(list(filter(lambda i:i["slot_date"]==str(tday),vaccinatelist)))
                print(slot_date)
                logging.info("Today Vaccinate Sloting Details!!!")

            if option==5:
                with open("vaccinate.csv","w+",encoding="UTF8",newline="") as p:
                    writer=csv.DictWriter(p,fieldnames=headerContent)
                    writer.writeheader()
                    writer.writerows(vaccinatelist)
                    logging.info("Save all the CSV File!!!")

            if option==6:
                for x in vaccinatelist:
                    message="COVID VACCINATION DETAILS\n"+str(x)
                    print(message)
                    connection=smtplib.SMTP("smtp.gmail.com",587)
                    connection.starttls()
                    connection.login("tamilarasiiprimed@gmail.com","Iprimed@123")
                    connection.sendmail("tamilarasiiprimed@gmail.com",x["mail_id"],message)
                    connection.quit
                    print("Mail Sent Successfully:)")
                
            if option==7:
                break
except ValueError:
    logging.error("Please Check Value int or string")

except IndexError:
    logging.error("Please Check Your Index")

except Exception:
    logging.error("Something Went Wrong")

finally:
    print("Äll Block Completed Successfully")






        
