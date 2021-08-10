
import writereadmodule
import searchingmodule
import logging 
logging.basicConfig(filename='error1.log',level=logging.ERROR)
while True:
    print("\n")
    print("Simple Hospital Management System \n")
    #print("\n")
    print("1.WRITE RECORD\n2.SHOW ALL RECORDS\n3.SEARCH BY SERIAL NUMBER")
    print("4.SEARCH BY CONTACT NUMBER\n5.SEARCH BY NAME")
    print("6.EXIT\n7.Exit")
    ch=int(input("\nPLEASE ENTER YOUR CHOICE:--"))
    try:
        if ch==1:
            writereadmodule.WriteHospital()
        if ch==2:
            writereadmodule.ReadHospital()
        if ch==3:
            n=input("PLEASE ENTER SERIAL NUMBER TO SEARCH:--")
            searchingmodule.SearchHospitalSno(n)
        if ch==4:
            n=input("PLEASE ENTER CONTACT NUMBER TO SEARCH:--")
            searchingmodule.SearchHospitalcontact(n)
        if ch==5:
            n=input("PLEASE ENTER DISEASE NAME TO SEARCH:--")
            searchingmodule.SearchName(n)
        if ch==6:  
            n=input("PLEASE ENTER SERIAL NUMBER FOR WHICH YOU NEED BILL")     
            print("Your bill for hospital ")  
            writereadmodule.mailing(n)
            print("BIll for hospital has been shared to your mail")
        if ch==7:
            break
            
    except:
       logging.error("you have entered wrong choice")