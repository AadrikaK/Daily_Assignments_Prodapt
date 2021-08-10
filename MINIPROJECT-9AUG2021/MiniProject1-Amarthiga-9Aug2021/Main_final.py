from sentinelsat import SentinelAPI
import pandas as pd

#For validation-Custome module 
from test1 import validation1

#For sending email-External modules
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

import logging


query= []

class sentinel:
    def login(self,user, password, api):
        self.user=user
        self.password=password
        self.api = api
        api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')
    
    def user_query(self,lat,long,footprint,product):
        self.lat=lat
        self.long=long
        self.footprint =footprint
        self.product = product

        


class sendemail:
    def Sendotp(self,useremail):
        self.useremail=useremail
        connection=smtplib.SMTP("smtp.gmail.com",587)
        connection.starttls()
        connection.login("amarproject2021@gmail.com", "Geo@2124")
        message= "Your One Time Password for the login session is 234566"
        connection.sendmail("amarproject2021@gmail.com",useremail,message)
        print("OTP has sent to user email ID")
        connection.quit()

class sendattachment(sendemail):
    def content(self,mail_content, sender_address, usermail):
        self.mail_content =mail_content
        self.sender_address =sender_address
        self.useremail =useremail

    def content(message):
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = useremail
        message['Subject'] = 'Semester Result of Student'

        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'SemResult.csv'
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'csv',Name=attach_file_name)
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)

        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)

        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, useremail, text)
        session.quit()
        print('Mail has been sent to parent')

    



Q = sentinel()
OTP = sendemail()

while(True):
    print("\n")
    print("Welcome to SentinalAPI")
    print("\n")
    print("1. Login to the page: ")
    print("2. Verify user identity: ")
    print("3. Query Satellite Data with latitude and longitude: ")
    print("4. View the available satellite data related to your querry: ")
    # print("5. View into GEOJSON file ")
    # print("6. GEOJSON Send an email to user")
    print("5. Exit")

    selection = int(input("Enter your choice: "))

    if selection == 1:
        print("\n")
        print("Please enter your login credentials: ")

        user = input("Type your User Name: ")
        password = input("Type your password: ")
        useremail = input("Type your email address: ")
        api = SentinelAPI(user, password, 'https://scihub.copernicus.eu/dhus')

        try:
            user_email = validation1.Valid3(useremail)
        
            print("Check email for otp")
            print("Click option 2 and verify your user identy to login")
        except:
            print("Try again")

        OTP.Sendotp(useremail)
        Q.login(user, password, api)

    if selection ==2:
        otpass =(input("Enter OTP: "))
        onetime=validation1.otp(otpass)

    if selection ==3:
        print("Now, you can query with latitude and longitude: ")
        lat=float(input("Enter latitude: "))
        long=float(input("Enter latitude: "))
        footprint = 'POINT(%s %s)' % (lat, long)
        product = api.query(footprint, 
                    date=('NOW-14DAYS', 'NOW'), 
                    platformname='Sentinel-2', 
                    producttype= 'S2MSI1C', 
                    area_relation='Contains',
                    limit=1
                    )

        Q.user_query(lat,long,footprint,product)

        # for value in product.values():
        #     tile = value['tileid']
            #print(value)
    if selection ==4:
        for value in product.values():
            tile = value['tileid']
            print(tile)
        print("\n")
        product_gdf = api.to_dataframe(product)
        print(product_gdf)

        product_gjson = api.to_geojson(product)
        print(product_gjson)

        # query.append(tile)
        # print(query)

    # if selection ==6:
        mail_content = """Dear user,
        """
        sender_address = 'amarproject2021@gmail.com'
        sender_pass = 'Geo@2124'

    if selection ==5:
        print("Exit")
        break















        
           









        






