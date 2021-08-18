import multiprocessing,logging
try:
    def Primenumbers():
        for num in range(2,500):
            #time.sleep(1)
            for i in range(2,num):
                if(num%i)==0:
                    break
            else:
                print(num,end=' ')

    def Palindromenumbers():
        for num in range(10,500):
            #time.sleep(1)
            temp=num
            reverse=0
            while(temp>0):
                rem=temp%10
                reverse=(reverse*10)+rem
                temp=temp//10
            if(num==reverse):
                print(num,end=' ')


    if(__name__=='__main__'):
        
        p1=multiprocessing.Process(target=Primenumbers)
        p2=multiprocessing.Process(target=Palindromenumbers)
        p1.start()
        p2.start()
        p1.join()
        p2.join()
        print(",,,,,")
except Exception:
    logging.error("something went wrong")
finally:
    print("completed")