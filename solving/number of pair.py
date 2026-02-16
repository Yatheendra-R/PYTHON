l1=[]
x1=int(input("Enter the number of elements in the list: "))
for i in range(0,x1):
    l1.append(int(input("Enter the number: ")))
l2=[]
x2=int(input("Enter the number of elements in the list: "))
for i in range(0,x2):
    l2.append(int(input("Enter the number: ")))
cnt=0
for i in l1:
    for j in l2:
        if(i**j > j**i):
            cnt+=1
print(cnt)

