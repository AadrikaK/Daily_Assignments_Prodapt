
import logging
def BookedUserInfo(Row,Seats,table_of_chart,Booked_ticket_Person):
    Enter_row = int(input('Enter Row number - \n'))
    Enter_column = int(input('Enter Column number - \n'))
    if Enter_row in range(1, Row+1) and Enter_column in range(1, Seats+1):
        if table_of_chart[str(Enter_row-1)][str(Enter_column)] == 'B':
            person = Booked_ticket_Person[Enter_row - 1][Enter_column - 1]
            print('Name - ', person['Name'])
            print('Phone number - ', person['Phone_No'])
            print('Gender - ', person['Gender'])
            print('Age - ', person['Age'])
                #print('Phone number - ', person['Phone_No'])
            print('Ticket Prize - ', '$', person['Ticket_prize'])
        else:
            print()
            print('---**---  Vacant seat  ---**---')
    else:
        print()
        print('***  Invalid Input  ***')
    print()
    logging.info("customer information showned")
