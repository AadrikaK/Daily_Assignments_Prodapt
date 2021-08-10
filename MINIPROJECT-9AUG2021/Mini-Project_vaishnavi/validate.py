import re
###### Validation Price ######
def val_price(price):
    val=re.search("^[1-9]",price)
    if val:
        return int(price)
    else:
        print('something went wrong')

###### Validation Name ######
def val_name(name):
    val1=re.search('^[A-Za-z]',name)
    if val1:
        return name
    else:
        print('You enter wrong Name')
        
###### Validation Email #######
def val_emailid(emailid):
    val2=re.search('^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$',emailid)
    if val2:
        return emailid
    else:
        print('You enter wrong emailid')
      