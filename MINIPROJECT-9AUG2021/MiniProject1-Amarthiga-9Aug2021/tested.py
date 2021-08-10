#For Validation
from test1 import validation1

#For sending email to user
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from shapely.geometry import MultiPolygon, Polygon
import pandas as pd
import folium
from sentinelsat import SentinelAPI, read_geojson, geojson_to_wkt
from datetime import date, datetime, time, timedelta
import logging
import requests
from collections import OrderedDict, defaultdict
import re
from sentinelsat.exceptions import (
    SentinelAPIError,
    QuerySyntaxError,
    ServerError,
    InvalidKeyError,
    QueryLengthError,
    InvalidChecksumError,
    UnauthorizedError,
)

class Sentinel:
    def __init__(self, user, password, api_url, timeout=None):

        self.session = requests.Session()
        if user and password:
            self.session.auth = (user, password)
        self.api_url =api_url if api_url.endswith("/") else api_url + "/"
        self.timeout = timeout

    def query(self,area=None,date=None,raw=None,area_relation="Intersects",order_by=None,limit=None,offset=0,**keywords):
        query = self.format_query(area, date, raw, area_relation, **keywords)
        





class Send_email:
    def content(self,mail_content, sender_address, sender_pass):
        self.mail_content =mail_content
        self.sender_address =sender_address
        self.sender_pass =sender_pass

        

class pass_message(Send_email):
    def content(message):
        
        message = MIMEMultipart()
        message['From'] = sender_address
        message['To'] = email
        message['Subject'] = 'Verify your user identity'
        message.attach(MIMEText(mail_content, 'plain'))
        attach_file_name = 'AmarthigsK_MiniProject-Abstract'
        attach_file = open(attach_file_name, 'rb')
        payload = MIMEBase('application', 'pdf',Name=attach_file_name)
        payload.set_payload((attach_file).read())
        encoders.encode_base64(payload)
        payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        message.attach(payload)
        session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
        session.starttls() #enable security
        session.login(sender_address, sender_pass) #login with mail_id and password
        text = message.as_string()
        session.sendmail(sender_address, email, text)
        session.quit()
        print('Mail has been sent to user email ID')

        
S = pass_message()






while(True):
    print("\n")
    print("Welcome to SentinalAPI")
    
    print("1. Login to the page: ")
    print("2. Verify user identity: ")
    print("2. Query Satellite Data with latitude and longitude: ")
    print("3. Query Satellite Data with date and time: ")
    print("4. View the available satellite data related to your querry: ")
    print("5. View into GEOJSON file ")
    print("6. Exit")

    selection = int(input("Enter your choice: "))

    if selection == 1:
        print("\n")
        print("Please enter your login credentials: ")
        
        user = input("Type your User Name: ")
        password = input("Type your password: ")
        email = input("Type your email address: ")
        
        user_email = validation1.Valid3(email)
        if user_email:
            print(" ")
        else:
            pass

        S.content()
          
        mail_content = """Your One Time Password for the login session is 234566"""
        sender_address = 'amarproject2021@gmail.com'
        sender_pass = 'Geo@2124'

    
    if selection ==2:
        otpass =int(input("Enter OTP: "))
        try:
            onetime=validation1.otp(otpass)
            if onetime:
                print("approved")
        except:
            logging.warning("Wrong OTP.")


    





