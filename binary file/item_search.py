import pickle,os
def MakeFile():
    with open("Items.dat","wb") as f:
        x=int(input("Enter the number of items"))
        for i in range(x):
            c=int(input("Enter the code: "))
            n=input("Enter the name: ")
            p=int(input("Enter the price: "))
            pickle.dump([c,n,p],f)
            
MakeFile()

def SearchRec(Code):
        with open("Items.dat","rb") as f1:
            try:
                check=0
                while True:
                    l=pickle.load(f1)
                    if l[0]==Code:
                        check+=1
                        print("Item code: ",l[0],"Item name: ",l[1],"Item price: ",l[2])
                
            except EOFError:
                pass
            if check==0:
                print("Code",Code,"is not present")
                print("Give the correct code")
                run()
def run():
    Code=int(input("Enter the code:"))
    SearchRec(Code)
run()
