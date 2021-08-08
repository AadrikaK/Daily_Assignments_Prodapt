import threading,time
x=input("enter a last number: ")

def primeno():
    if x>1:
        for i in range(2,x):
            if(x%i)==0:
                break
            else:
                print(i,end=" ")
                break

def palindrome():
    y=""
    for i in range(1,x):
        y=i+y
        if(x==y):
            break
        else:
            print(x,end=" ")

t1=threading.thread(target=primeno)
t2=threading.thread(target=palindrome)
t1.start()
t2.start()