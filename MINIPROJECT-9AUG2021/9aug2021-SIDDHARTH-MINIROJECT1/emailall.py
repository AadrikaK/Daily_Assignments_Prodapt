import smtplib
import validate
def emailAll():
    emailme=input("Enter your email id: ")
    if validate.validateemail(emailme):
            connection=smtplib.SMTP("smtp.gmail.com",587)
            connection.starttls()
            connection.login("hariompateldada@gmail.com","Sparsh@01")
            message="hello all, I hope you all are doing great.hello all, I hope you all are doing great."
            connection.sendmail("hariompateldada@gmail.com",["ridhimathur10@gmail.com","siddhugupta15@gmail.com"],message)
            print("Email has sent succesfully")
            connection.quit()
    else:
         print("Please enter valid mail")
