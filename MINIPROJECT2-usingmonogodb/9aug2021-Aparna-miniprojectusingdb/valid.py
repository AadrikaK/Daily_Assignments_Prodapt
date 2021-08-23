import re, logging
logging.basicConfig(filename='error.log',level=logging.ERROR)

def validation_of_traindetails(train_name,start_station,dest_station):
    # valid1=re.match("[0-9]{0,7}$",train_no)
    valid2=re.match("([a-z]+)([a-z]+)([a-z]+)$",train_name)
    valid3=re.match("([a-z]+)([a-z]+)([a-z]+)$",start_station)
    valid4=re.match("([a-z]+)([a-z]+)([a-z]+)$",dest_station)
    
    try:
        if valid2 and valid3 and valid4:
            return True
        else:
            return False
    except:
        logging.error("Invalid train details, enter correct details and try again...")


def validatemail(email):
    valemail=re.match("^\w+[\._]?\w+[@]\w+[.]\w{2,3}$",email)
    if valemail:
        return True
    else:
        return False


def validation_of_passenger(passenger_name,age,email,from_station,to_station):
    regex='^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    # val1=re.match("[0-9]{0,7}$",passenger_id)
    val2=re.match("([a-z]+)([a-z]+)([a-z]+)$",passenger_name)
    val3=re.match("[0-9]{0,3}$",age)
    val4=re.match(regex,email)
    # val5=re.match("^9[0-9]{0,9}$",phone_no)
    val6=re.match("([a-z]+)([a-z]+)([a-z]+)$",from_station)
    val7=re.match("([a-z]+)([a-z]+)([a-z]+)$",to_station)
    
    try:
        if val2 and val3 and val4 and val6 and val7:
            return True
        else:
            return False
    except:
        logging.error("Invalid passenger details, enter correct details and try again...")

