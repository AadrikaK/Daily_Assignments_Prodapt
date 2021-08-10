import re,csv,logging
donorlist=[]
patientlist=[]
try:
    header=["dname","did","dphno","daddress","dage","dbgroup"]
    header1=["pname","pid","pbgroup","page","pphno","paddress"]
    class BloodBankMgt:
            def donor(self,dname,did,dphno,daddress,dage,dbgroup):
                self.dname=dname
                self.did=did
                self.dphno=dphno
                self.daddress=daddress
                self.dage=dage
                self.dbgroup=dbgroup
            def patient(self,pname,pid,pbgroup,page,pphno,paddress):
                self.pname=pname
                self.pid=pid
                self.pphno=pphno
                self.paddress=paddress
                self.page=page
                self.pbgroup=pbgroup   
            def adddonordetail(self,dname,did,dphno,daddress,dage,dbgroup):
                dict1={"dname":dname,"did":did,"dphno":dphno,"daddress":daddress,"dage":dage,"dbgroup":dbgroup} 
                donorlist.append(dict1)
            def addpatientdetail(self,pname,pid,pphno,paddress,page,pbgroup):
                dict2={"pname":pname,"pid":pid,"pphno":pphno,"paddress":paddress,"page":page,"pbgroup":pbgroup} 
                patientlist.append(dict2)
    def validated(dname,did,dphno,daddress):
        valdonorname=re.search("^[A-Z]{1}[A-Z]{0,25}$",dname)
        valdid=re.search("^[0-9]{1,3}$",did)
        valdphno=re.search("^[7-9][0-9]{9}$",dphno)
        valdaddress=re.search("^[A-Z]{1}[A-Z]{0,200}$",daddress)
        valdbgroup=re.search("^[A-Z]{1,2}[+]|[-]$",dbgroup)
        if valdonorname and valdid and valdphno and valdaddress  :
            return True
        else:
            return False    
    def validatep(pname,pid,pphno,paddress):
        valpatientname=re.search("[A-Z]{1}[A-Z]{0,25}$",pname)
        valpid=re.search("[0-9]{1,3}$",pid)
        valpphno=re.search("^[7-9][0-9]{9}$",pphno)
        valpaddress=re.search("[A-Z]{1}[A-Z]{0,200}$",paddress)
        # valpbgroup=re.search("^[A-Z]{1,2}[+]|[-]$",pbgroup)
        if valpatientname and valpid and valpphno and valpaddress:
            return True
        else:
            return False
    obj=BloodBankMgt()
    if(__name__=="__main__"):
        while True:
            print("1.Add Donor details")
            print("2.Display Donor details") 
            print("3.Search Donor by ID")
            print("4.Add patient details")
            print("5.Display Patient details")
            print("6.Search Patient based on name")
            print("7.Save Donor details")
            print("8.Save Patient details")
            print("9.Exit")
            choice=int(input("Enter your option : "))
            if choice==1:
                dname=input("Enter the DONOR NAME : ") 
                did=input("Enter the DONOR ID : ") 
                dphno=input("Enter the DONOR PH NO : ")
                daddress=input("Enter the DONOR ADDRESS : ")
                dage=input("Enter the DONOR AGE : ")
                dbgroup=input("Enter the DONOR Blood GROUP : ")
                if validated(dname,did,dphno,daddress)==True:
                    obj.adddonordetail(dname,did,dphno,daddress,dage,dbgroup) 
                else:
                    logging.error("VALIDATION ERROR!!!")
                    break
            if choice==2:
                print(donorlist)
            if choice==3:
                
                ddid=input("Enter the Donor ID to search : ")
                print(list(filter(lambda i:i["did"]==ddid,donorlist)))
                
            if choice==4:
                pname=input("Enter the PATIENT NAME : ") 
                pid=input("Enter the PATIENT ID : ") 
                pphno=input("Enter the PATIENT PH NO : ")
                paddress=input("Enter the PATIENT ADDRESS : ")
                page=input("Enter the PATIENT AGE : ")
                pbgroup=input("Enter the PATIENT Blood GROUP : ")
                if validatep(pname,pid,pphno,paddress)==True:
                    obj.addpatientdetail(pname,pid,pbgroup,page,pphno,paddress) 
                else:
                    logging.error("VALIDATION ERROR!!!")
                    break
            if choice==5:
                print(patientlist)
            if choice==6:
                ppname=input("Enter the Patient Name to search : ")
                print(list(filter(lambda i:i["pname"]==ppname,patientlist)))
            if choice==7:
                with open('donor.csv','w+',encoding='UTF8',newline='') as s:
                    writer = csv.DictWriter(s,fieldnames=header)
                    writer.writeheader()
                    writer.writerows(donorlist)
            if choice==8:
                with open('patient.csv','w+',encoding='UTF8',newline='') as s:
                    writer = csv.DictWriter(s,fieldnames=header1)
                    writer.writeheader()
                    writer.writerows(patientlist)
            if choice==9:
                break 
except:
    logging.error("OOPS!! Something is wrong") 
finally:
    print("Thank you")                                                                      