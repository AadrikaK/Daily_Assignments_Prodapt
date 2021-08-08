
import re
import csv

headerContent=['total','name','rollno','admino','hindi','english','maths']

studentlist=[]

class StudentDetails:   
    def addstudent(self,name,rollno,admino,hindi,english,maths):
        totalmarks=hindi+english+maths
        dic={"total":totalmarks,"name":name,"rollno":rollno,"admino":admino,"hindi":hindi,"english":english,"maths":maths}
        studentlist.append(dic) 
    

obj1=StudentDetails()

while(True):    #menudriven
    print("1 Add student:")
    print("2 search student rollno:")
    print("3 display student api:")
    print("4 ranking:")
    print("5 save a file:")
    print("6 exit:")
    choice=int(input("enter a option:"))
   

    if choice==1:
        name=input("enter name:")
        rollno=int(input("enter roll no:"))
        admino=int(input("enter admino no:"))
        hindi=int(input("enter hindi marks:"))
        maths=int(input("enter maths marks:"))
        english=int(input("enter english marks:"))

        def val(name,rollno,admino):
            valn=re.search("^[A-Z]",name)
            valr=re.search('^[1-9]',rollno)
            vala=re.search('^[0-9]',admino)
            if valn and valr and vala:
                return True
            else:
                return False

        obj1.addstudent(name,rollno,admino,hindi,english,maths)

    if choice==2:
        srollno=int(input("enter the rollno to search:"))
        print(list(filter(lambda i:i["rollno"]==srollno,studentlist)))
    
    if choice==3:
        print(studentlist)

    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))

    if choice==5:
        with open('student.csv','w+',encoding='UTF8',newline='') as s:
            writer=csv.DictWriter(s,fieldnames=headerContent)
            writer.writeheader()
            writer.writerows(studentlist)
       
    if choice==5:
        break