import re
import buyticket
def isvalidmob():
    r=re.match("(0|91)?[-\s]?[6-9]\d{9}",buyticket.person_detail['Phone_No'])
    if (r):
        return True
    else:
        return False

def isvalidname():
    vallast=re.match(r'^([a-z]+)( [a-z]+)*( [a-z]+)*$',buyticket.person_detail['Name'])
    if (vallast):
        return True
    else:
        return False

def validateemail(email):
    r1= re.match(r"[\w-]{1,20}@\w{2,20}\.\w{2,3}$",email)
    if (r1):
        return True
    else:
        return False


