def push(vi):

    x=int(input("v-no"))
    x1=input("date")
    x2=input("name")
    x3=input("gender")
    x4=int(input("age"))
    if x4>14:
        if x4<20:
            stat.append([x,x1,x2,x3,x4])

stat=[]

for i in range(int(input("enter the number of ppl"))):
    x=int(input("v-no"))
    x1=input("date")
    x2=input("name")
    x3=input("gender")
    x4=int(input("age"))
    stat.append([x,x1,x2,x3,x4])
def pop():
    cntm=0
    cntf=0
    print(stat)
    while len(stat)>0:
        poped=stat.pop()
        if poped[3].lower()=="m":
            cntm+=1
        elif poped[3].lower()=="f":
            cntf+=1
    print("Done")
    print("fe",cntf)
    print("male",cntm)
while True :
    print("MENU")
    print("1-push(or)add")
    print("2-pop and count M and F")
    print("3-Exit")
    ch=int(input("Enter your choice: "))
    if ch==1:
        push(stat)
    elif ch==2:
        pop()
    elif ch==3:
        break
    else:
        print("invalid")

