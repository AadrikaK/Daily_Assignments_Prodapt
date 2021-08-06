import multiprocessing,time,logging
try:
    def primeNumbers():
        for i in range(2,500):
            #tine.sleep(1)
            if i>1:
                for j in range(2,i):
                    if i%j==0:
                        break
                    else:
                        print("primenumbers:",i,end='')
    def palindrome():
        for i in range(10,500):
            temp=i
            rev=0
            while(temp>0):
                rem=temp%10
                rev=(rev*10)+rem
                temp=temp//10
                if(i==rev):
                    print("palindrome:",i,end='')

    if __name__ == "__main__":
        p1=multiprocessing.Process(target=primeNumbers)
        p2=multiprocessing.Process(target=palindrome)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print("..........")
except Exception:
    logging.error("Something Wrong!")