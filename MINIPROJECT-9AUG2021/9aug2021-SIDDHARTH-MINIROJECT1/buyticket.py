#from mainfile1 import Booked_seat
import validate
import sys

def BuyTicketEnjoy(Ro,St,table_chart,Booked_seat,Total_Income,Booked_ticket_Person):
    Row_number = int(input('Enter Row Number - \n'))
    Column_number = int(input('Enter Column Number - \n'))
    if Row_number in range(1, Ro+1) and Column_number in range(1, St+1):
        if table_chart[str(Row_number-1)][str(Column_number)] == 'S':
            if Ro*St <= 60:
                prize_of_ticket = 250
            elif Row_number <= int(Ro/2):
                prize_of_ticket = 100
            else:
                prize_of_ticket = 80
            print('prize_of_ticket - ', 'Rs.', prize_of_ticket)
            confirm = input('yes for booking and no for Stop booking - ')
            person_detail = {}
            if confirm == 'yes':
            
                person_detail['Name'] = input('Enter Name - ')
                person_detail['Phone_No'] = input('Enter Phone number - ')
                if validate.isvalidname and validate.isvalidmob:
                        person_detail['Gender'] = input('Enter Gender - ')
                        person_detail['Age'] = input('Enter Age - ')
                            #person_detail['Phone_No'] = input('Enter Phone number - ')
                        #email=input("Please Enter the Customer Email Id :")
                        person_detail['Ticket_prize'] = prize_of_ticket
                        table_chart[str(Row_number-1)][str(Column_number)] = 'B'
                        Booked_seat += 1
                        Total_Income += prize_of_ticket
                else:
                    sys.exit()
                    
            else:
                sys.exit()
            Booked_ticket_Person[Row_number-1][Column_number-1] = person_detail
            print('Booked Successfully')
        else:
            print('This seat already booked by some one')
    else:
        print()
        print('***  Invalid Input  ***')
    print()

