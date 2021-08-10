import timeit,logging
try:
    list = [19,2,31,45,6,11,121,27]
     
        
    def sort():
        def bubblesort():
            for iter_num in range(len(list)-1,0,-1):
                for idx in range(iter_num):
                    if list[idx]>list[idx+1]:
                        temp=list[idx]
                        list[idx]=list[idx+1]
                        list[idx+1]=temp
                        

    if(__name__=='__main__'):
        print(timeit.timeit(sort,number=10000))
         

except:
    logging.error("something wrong")         