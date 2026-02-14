import pickle,os
with open("Tele.dat","wb") as f:
    x=int(input("Enter the number of people"))
    for i in range(x):
        phnum=int(input("Enter the phone number"))
        cname=input("Enter the name")
        areacode=int(input("Enter the area code"))
        d={"phonenumber":phnum,"name":cname,"areacode":areacode}
        pickle.dump(d,f)

with open("Tele.dat","rb") as f1:
    with open("back.dat","wb") as f2:

        try:
            cnt=0
            while True:
                d1=pickle.load(f1)
                if d1['areacode']==11:
                    pickle.dump(d1,f2)
                    cnt+=1
                    
        except EOFError:
            pass
        
if cnt==0:
    print("no record found as areacode of 11")

##check##
with open("back.dat","rb") as f3:
    try:
        while True:
                d3=pickle.load(f3)
                print(d3)
    except EOFError:
            pass
