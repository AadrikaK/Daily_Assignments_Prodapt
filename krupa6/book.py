import re,logging

booklist=[]
logging.basicConfig(filename='bookfile.log',level=logging.DEBUG)
try:
    class book:   
        def addbook(self,title,description,price,distributer,publisher):
            dic={"title":title,"description":description,"price":price,"distributer":distributer,"publisher":publisher}
            booklist.append(dic) 


    obj1=book()

    while(True):   
        print("1 add book :")
        print("2 view book :")
        print("3 sorted book on basic of alphabet :")
        print("4 search book using title:")
        print("5 exit:")
        choice=int(input("enter a option: "))
    

        if choice==1:
            title=input("enter title of book :")
            description=input("enter description:")
            price=int(input("enter price:"))
            distributer=input("enter the distributer details:")
            publisher=input("enter the publisher:")

            def val(title,description,price):
                val1=re.search("^[A-Z]?[a-n]",title)
                val2=re.search('^[1-9]',price)
                val3=re.search('^[A-Z]',description)
                if val1 and val2 and val3:
                    return True
                else:
                    return False
            obj1.addbook(title,description,price,distributer,publisher)

        if choice==2:
            view=input("enter the book title to view :")
            print(list(filter(lambda i:i["title"]==view,booklist)))
        
        if choice==3:
            print(sorted(booklist,key=lambda i:i["title"],reverse=True))
            print(booklist)

        if choice==4:
            searchb=input("enter the book title to search:")
            print(list(filter(lambda i:i["title"]==searchb,booklist)))
        

        if choice==5:
            break
        logging.debug("completed")
except Exception:
    logging.error("wrong")
finally:
    print("completed")
