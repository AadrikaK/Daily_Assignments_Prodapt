import timeit
li=[1,2,3,4]


try:
    #selection sort
    def selection():
        length=len(li)
        for i in range(length-1):
            min=li[i]
            pos=i
            for j in range(i+1,length):
                if li[j]<min:
                    min=li[j]
                    pos=j
            li[i],li[pos]=li[pos],li[i]
        pass
    print(timeit.timeit(selection,number=10000))

    #bubble sort

    def bubble():
        length=len(li)
        i=li[0]
        j=li[0]
        for i in range(length-1):
            for j in range(length-i-1):
                if li[j]>li[j+1]:
                    li[j],li[j+1]=li[j+1],li[j]
                pass
    print(timeit.timeit(bubble,number=10000))

    #insertion sort

    def insert():
        length=len(li)
        for i in range(1,length):
            item=li[i]
            j=i-1
            while(j>=0 and li[j]>item):
                li[j+1]=li[j]
                j=j-1
                while(j>=0 and li[j]>item):
                    li[j+1]=li[j]
                    j=j-1
                li[j+1]=item
            pass
    print(timeit.timeit(insert,number=10000))

except Exception:
    print("error occured")     
finally:
    print("completed")          



