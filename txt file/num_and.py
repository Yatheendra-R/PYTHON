
def num():
    with open("no_and","r") as f:
        x=f.read().split()
        c=0
        print(x)
        for k in x:
            if k=="and":
                c+=1
        print(c)
        
num()


