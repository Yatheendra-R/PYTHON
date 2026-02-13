def wfile():
    with open("book.txt","w") as f:
        x="yes"
        while x=="yes":
            bno=int(input("Enter the book number: "))
            print()
            bna=input("Enter the book name: ")
            print()
            an=input("Enter the author name: ")
            print()
            bp=int(input("Enter the book price: "))
            print()
            f.write("book number: "+str(bno)+" ,book name: "+bna+" ,author name: "+an+" ,book price: "+str(bp)+"\n")

            x=input("do you want to continue(yes/no): ").lower()
            
wfile()
