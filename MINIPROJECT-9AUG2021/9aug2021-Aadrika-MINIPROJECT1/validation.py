################# VALIDATION FUNCTION ###################################################
import re, logging
logging.basicConfig(filename='error2.log',level=logging.ERROR)

def validation_of_Patients(sno,name,phone ,email):
    reg = '^\w+[\._]?\w+[@]\w+[.]\w{2,3}$'
    
    val1=re.match("([a-z]+)([a-z]+)([a-z]+)$",name)
    val2=re.match("[0-9]{0,7}$",sno)
    val3=re.match("^9[0-9]{0,9}$",phone)
    val4=re.match(reg,email)
    
  
    try:
        if val1 and val2 and val3 and val4 :
            return True
        else:
            return False
    except:
        logging.error("Some data is not validated please try again later")
    else:
        logging.info("all done ")