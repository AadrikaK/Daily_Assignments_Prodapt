import csv
def SearchHospitalSno(n):
     with open("hospital.csv","r",encoding="utf-8") as f:
        read=csv.DictReader(f)
        for d in read:
            if d["Serial number"]==n:
                print(d)
def SearchHospitalcontact(n): 
    try:
        with open("hospital.csv","r",encoding="utf-8") as f:
            read=csv.DictReader(f)
            for d in read:
                if d["Phone number:"]==n:
                    print(d)
    except:
        print("no results found")


def SearchName(n): 
    try: 
        with open("hospital.csv","r",encoding="utf-8") as f:
            read=csv.DictReader(f)
            for d in read:
                if d["Patinet's Name"]==n:
                    print(d)
    except:
        print("no results found")
            