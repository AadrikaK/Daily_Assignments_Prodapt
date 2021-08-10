import mainfile1
def showSeats():

    if mainfile1.Seats < 10:

        for seat in range(mainfile1.Seats):
            print(seat, end='  ')
        print(mainfile1.Seats)
    else:
        for seat in range(10):
            print(seat, end='  ')
        for seat in range(10, mainfile1.Seats):
            print(seat, end=' ')
        print(mainfile1.Seats)
    if mainfile1.Seats < 10:
        for num in mainfile1.table_of_chart.keys():
            print(int(num)+1, end='  ')
            for no in mainfile1.table_of_chart[num].values():
                print(no, end='  ')
            print()
    else:
        count_num = 0
        for num in mainfile1.table_of_chart.keys():
            if int(list(mainfile1.table_of_chart.keys())[count_num]) < 9:
                print(int(num)+1, end='  ')
            else:
                print(int(num)+1, end=' ')
            count_key = 0
            for no in mainfile1.table_of_chart[num].values():
                if int(list(mainfile1.table_of_chart[num].keys())[count_key]) <= 10:
                    print(no, end='  ')
                else:
                    print(no, end='  ')
                count_key += 1
            count_num += 1
            print()
    print('Vacant Seats = ', mainfile1.Total_seat - mainfile1.Booked_seat)
    print()
