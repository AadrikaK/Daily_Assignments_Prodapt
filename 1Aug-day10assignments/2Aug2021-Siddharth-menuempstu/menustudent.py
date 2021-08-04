import time
import re
studentlist=[]
class Student:
    def studentdetails():
         name=" "
         rollnum=0
         adminnum=0
class marks:
    def stumarks():
        eng=0
        hindi=0
        maths=0
        science=0
    

   
class studentdetails(Student,marks):
    def addstudentdetails(self,name,rollnum,adminnum,eng,hindi,maths,science):
        total=eng+hindi+maths+science
        current_local_time=time.strftime("%H:%M:%S",time.localtime())
        dict1={"name":name,"rollnum":rollnum,"adminnum":adminnum,"eng":eng,"hindi":hindi,"maths":maths,"science":science,"total":total,"addedon":current_local_time}
        studentlist.append(dict1)
obj1=studentdetails()


def validation_name(name,roll):
    val=re.match("([a-z]+)([a-z]+)([a-z]+)$",name)
    val2=re.match("[0-9]{0,7}$",roll)
    if val and val2:
        return True
    else:
        return False


while(True):
    print("1. Add Students:")
    print("2. display student details: ")
    print("3. search student using roll number")
    print("4. Ranking")
    print("5. exit")
    choice=int(input("enter your choice: "))
    
    if choice==1:
        while(True):
            name=input("Enter your name: ")
            rollnum=(input("enter your rollnum: "))
            if validation_name(name,rollnum):
                adminnum=int(input("enter your admin num: "))
                eng=int(input("enter english marks: "))
                hindi=int(input("enter hindi marks: "))
                maths=int(input("enter maths marks: "))
                science=int(input("enter science marks: "))

                obj1.addstudentdetails(name,rollnum,adminnum,eng,hindi,maths,science)
            else:
                print("PLease Try again by entering valid name and rollno")
                continue
            break
        
    if choice==2:
        print(studentlist)
    if choice==3:
        srollno=input("Enter roll number to search: ")
        print(list(filter(lambda i:i["rollnum"]==srollno,studentlist)))
    if choice==4:
        print(sorted(studentlist,key=lambda i:i["total"],reverse=True))
    if choice==5:
        break