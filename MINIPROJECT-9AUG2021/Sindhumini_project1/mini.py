import csv
import re
import logging
try:

candidatelist = []
voterlist = []
headerContent1 = ["candname", "candgender","candaddress", "candparty", "candcity"]
headerContent2 = ["votid", "votname", "votwardno", "votaddress", "votphoneno"]


class ElectionManagement:
    def candidate(self, candname, candgender, candaddress, candparty, candcity):
        self.candname = candname
        self.candgendr = candgender
        self.candaddress = candaddress
        self.candparty = candparty
        self.candcity = candcity

    def voter(self, votname, votid, votwardno, votaddress, votphoneno):
        self.votid = votid
        self.votname = votname
        self.votwardno = votwardno
        self.votaddress = votaddress
        self.votphoneno = votphoneno

    def addcandidatedetails(self, candname, candgender, candaddress, candparty, candcity):
        dict1 = {"candname": candname, "candgender": candgender,
                 "candaddress": candaddress, "candparty": candparty, "candcity": candcity}
        candidatelist.append(dict1)

    def addvoterdetails(self, votname, votid, votwardno, votaddress, votphoneno):
        dict2 = {"votname": votname, "votid": votid, "votwardno": votwardno,
                 "votaddress": votaddress, "votphoneno": votphoneno}
        voterlist.append(dict2)


def validate(candname, candgender, candaddress, candparty, candcity):
    valcandname = re.search("^[A-Z]{1}[A-Z]{0,25}$", candname)
    valcandaddress = re.search("^[A-Z]{1}[A-Z]{0,200}$", candaddress)
    valcandparty = re.search("^[A-Z]{1}[A-Z]{0,25}$", candparty)
    valcandcity = re.search("^[A-Z]{1}[A-Z]{0,200}$", candcity)
    valcandgender = re.search("FEMALE|MALE", candgender)
    if valcandname and valcandaddress and valcandparty and valcandcity and valcandgender:
        return True
    else:
        return False


def validatevote(votname, votid, votwardno, votaddress, votphoneno):
    valvotname = re.search("[A-Z]{1}[A-Z]{0,25}$", votname)
    valvotid = re.search("[0-9]{1,3}$", votid)
    valvotwardno = re.search("[0-9]{1,3}$", votwardno)
    valvotaddress = re.search("[A-Z]{1}[A-Z]{0,200}$", votaddress)
    valvotphoneno = re.search("^[7-9][0-9]{9}$", votphoneno)
    if valvotname and valvotid and valvotwardno and valvotaddress and valvotphoneno:
        return True
    else:
        return False


obj = ElectionManagement()
print("1)enter Candidate details")
print("2)Search Candidate by party name")
print("3)Save to file")
print("4)enter Voter details")
print("5)Search Voter by ID")
print("6)Save to file")
print("7)Exit")
while True:
    choice = int(input("Enter your option : "))
    if choice == 1:
        candname = input("Enter the candidate name : ")
        candgender = input("Enter candidate gender : ")
        candaddress = input("Enter candidate address : ")
        candparty = input("Enter candidate party : ")
        candcity = input("Enter candidate city : ")
        if validate(candname, candgender, candaddress, candparty, candcity):
            obj = ElectionManagement()
            obj.candidate(candname, candgender,
                          candaddress, candparty, candcity)
            obj.addcandidatedetails(
                candname, candgender, candaddress, candparty, candcity)
            print(candidatelist)
        else:
            logging.error("invalid data enter a valid data")

    elif choice == 2:
        candparty = input("Enter the party to search : ")
        print(
            list(filter(lambda i: i["candparty"] == candparty, candidatelist)))

    elif choice == 3:
        with open('candidate.csv', 'w+', encoding='UTF8', newline='') as s:
            writer = csv.DictWriter(s, fieldnames=headerContent1)
            writer.writerows(candidatelist)

    elif choice == 4:
        votname = input("Enter voter name: ")
        votid = input("Enter voter ID : ")
        votwardno = input("Enter voter wardno : ")
        votaddress = input("Enter voter address : ")
        votphoneno = input("Enter voter phoneno : ")
        if validatevote(votname, votid, votwardno, votaddress, votphoneno):
            obj.voter(votname, votid, votwardno, votaddress, votphoneno)
            obj.addvoterdetails(
                votname, votid, votwardno, votaddress, votphoneno)
            print(voterlist)
        else:
            logging.error("invalid data enter a valid data")

    elif choice == 5:
        votid = input("Enter the voterid to search : ")
        print(list(filter(lambda i: i["votid"] == votid, voterlist)))

    elif choice == 6:
        with open('voter.csv', 'w+', encoding='UTF8', newline='') as s:
            writer = csv.DictWriter(s, fieldnames=headerContent2)
            writer.writerows(voterlist)

    elif choice == 7:
        print("Exit")
        break

    else:
        print("Please enter correct choice.\nEnter 7 to exit otherwise.")
except Exception:
    logging.error("Something Went Wrong!")
finally:
    print("code completed successfully")