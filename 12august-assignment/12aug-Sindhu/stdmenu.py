import pymongo,re
client=pymongo.MongoClient("mongodb://localhost:27017")
mydatabase=client['StudentDb']
collection_name=mydatabase['student1']
studentlist=[]
dict1={}

class StudentDetails:
    def _init_(self,name,rollno,std,englishmark,mathsmark,socialmark,sciencemark):
        self.name=name
        self.rollno=rollno
        self.std=std
        self.englishmark=englishmark
        self.hindimark=hindimark
        self.mathsmark=mathsmark
        self.socialmark=socialmark
        self.sciencemarkk=sciencemarkk
    def addstudentdetail(self,name,rollno,std,englishmark,mathsmark,socialmark,sciencemark):
        totalmarks=englishmark+mathsmark+sciencemark+socialmark
        dict1 ={"total":totalmarks,"name":name,"rollno":rollno,"std":std,"english":englishmark,"maths":mathsmark,"science":sciencemark,"social":socialmark}   
        studentlist.append(dict1)
# collection_name.insert_one(dict1)
obj=StudentDetails()
def validate(vname,vrollno):
    name=re.search("[a-z]{1}[^a-z]{0,25}$",dict1["valname"])
    rollno=re.search("[0-9]{0,7}$",["valrollno"])
    if name1 and rollno1:
        return True
    else:
        return False

while True:
    print("1. Add student details : ")
    print("2. View all students total marks :")
    print("3. Search Student with std and rollno :")
    print("4. Update Student data with marks based on rollno and std :")
    print("5. Find average marks of english based on std :")
    print("6. Delete Students based on rollno and std : ")
    print("7. Exit:")
    
    ch=int(input("Enter your choice :"))
    if(ch==1):
        name=input("Enter name :")
        rollno=int(input("Enter rollno :"))
        std=input("Enter std :")
        englishmark=int(input("Enter your English marks : "))
        mathsmark=int(input("Enter your maths marks : "))
        sciencemark=int(input("Enter your Science marks: "))
        socialmark=int(input("Enter your Social Marks : "))
        if validate(name,rollno):
                obj =StudentDetail()
                donorlist.append(obj.addblooddonordetails(name,rollno,std,englishmark,mathsmark,socialmark,sciencemark))
    if(ch==2):
        result=collection_name.find({"flag":1})
        for i in result:
            print(i)
    if(ch==3):
        rollno=input("Search the student rollno :")
        std=input("Search the student std :")
        result=collection_name.find({"std":std,"rollno":rollno})
        for i in result:
            print(i)
    if(ch==4):
        name:input("Enter the name:")
        rollno=input("Enter the student rollno : ")
        std=input("Enter the student std :")
        englishmark=input("Enter the english mark:")
        mathsmark=input("Enter the mathmark:")
        result=collection_name.update_one({"std":std,"rollno":rollno},{"$set":{"name":name,"englishmark":englishmark,"mathsmark":mathsmark}})
        print(result)
        
    if(ch==5):
        std=input("Enter the std:")
        result=collection_name.aggregate([{"$group":{"_id":None,"average":{"$avg":"$english"}}}])
        for i in result:
            print(i)

    if(ch==6):
        rollno=input("Enter the student rollno :")
        std=input("Enter the student rollno :")
        result=collection_name.delete_many({"rollno":rollno,"std":std})
        print(result)
        
    if(ch==7):
        break
    
