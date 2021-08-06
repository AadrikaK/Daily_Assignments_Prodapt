import threading,time,logging
try:
    def Prime():
        for i in range(10,500):
            time.sleep(1)
            for j in range(2,i):
                if(i%j==0):
                    break
            else:
                print(i,"prime number")
    def palindrome():
        for i in range(10,500):
            temp=i
            rev=0
            while i>0:
                time.sleep(1)
                rem=i%10
                rev=rev*10+rem
                i=i//10
            if temp==rev:
                print(temp,"palindrome")
        
            else:
                print(temp,"not a palindrome")
    if(__name__=="__main__"):
        t1=threading.Thread(target=Prime)
        t2=threading.Thread(target=palindrome)
        t1.start()
        t2.start()
        t1.join()
        t2.join()
except:
    logging.error("Can not able to process")