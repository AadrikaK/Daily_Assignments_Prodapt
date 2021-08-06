import threading,time,logging
try:
    def primeNumbers():
        for i in range(2,500):
            # time.sleep(3)
            if i>1:
                for j in range(2,i):
                    if i%j==0:
                        break
                    else:
                        print("primenumbers:",i,end='')
    def palindrome():
        for i in range(10,500):
            # time.sleep(3)
            temp=i
            rev=0
        while(temp>0):
            rem=temp%10
            rev=(rev*10)+rem
            temp=temp//10
            if(i==rev):
                print("palindrome:",i,end='')
    if(__name__=='__main__'):
        t1=threading.Thread(target=primeNumbers)
        t2=threading.Thread(target=palindrome)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
        print("..........")
except Exception:
    logging.error("Something Wrong!")
