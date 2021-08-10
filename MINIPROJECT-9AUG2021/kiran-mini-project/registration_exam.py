import re,csv,logging
try:
    headerContent=["name","roll","college","mailid","exam_type","fee","reg_open_date","reg_closing_date"]
    participants_list=[]
    class ExamRegistration:
        def addParticipants(self,name,roll,college,mailid,exam_type,fee,reg_open_date,reg_closing_date):
            dict={"name":name,"roll":roll,"college":college,"mailid":mailid,"exam_type":exam_type,"fee":fee,"reg_open_date":reg_open_date,"reg_closing_date":reg_closing_date}
            participants_list.append(dict)
    obj=ExamRegistration()
    def validation(name,roll,mailid):
        val1=re.match("[A-Z][a-z]{2,20}$",name)
        val2=re.match("^[0-9]{0,7}$",roll)
        val3=re.match("^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$",mailid)
        if val1 and val2 and val3:
            return True
        else:
            return False

    while(1):
        print("1.add participants")
        print("2.view all participants")
        print("3.search the  participant by name")
        print("4.list all the participants who registered first")
        print("5.save to csv file")
        print("6.Exit")
        
        choice=int(input("enter your choice:"))

        if choice==1:
            while(True):
                name=input("Enter the name:")
                roll=input("Enter the rollno:")
                mailid=input("Enter the mailid:")
                if validation(name,roll,mailid):
                    # name=input("Enter the name:")
                    # roll=input("Enter the rollno:")
                    # mailid=input("Enter the mailid:")
                    college=input("Enter the college name:")
                    exam_type=input("Enter the type of exam:")
                    fee=input("enter the amount:")
                    reg_open_date=input("Enter the registration opening date:")
                    reg_closing_date=input("Enter the registration closing date:")
                    obj.addParticipants(name,roll,college,mailid,exam_type,fee,reg_open_date,reg_closing_date)
                else:
                    print("please enter valid details")
                    continue
                break

        if choice==2:
            print(participants_list)

        if choice==3:
            pname=input("Enter the name to search:")
            print(list(filter(lambda i:i["name"]==pname,participants_list)))

        if choice==4:
            print("list all the participants who registered first:")
            print(sorted(participants_list,key=lambda i:i["reg_open_date"]))

        if choice==5:
            with open("Registration.csv","w+",encoding="UTF8") as r:
                writer=csv.DictWriter(r,fieldnames=headerContent)
                writer.writeheader()
                writer.writerows(participants_list)

        if choice==6:
            break

except Exception:
    logging.error("something went wrong")
finally:
    print("completed")
