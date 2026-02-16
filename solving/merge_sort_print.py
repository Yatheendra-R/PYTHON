l1=[]
x1=int(input("Enter the number of element present in first list: "))
for i in range(0,x1):
       l1.append(int(input("Enter the number: ")))
l2=[]
x2=int(input("Enter the number of element present in second list: "))
for i in range(0,x2):
    l2.append(int(input("Enter the number: ")))
print(l1)
print(l2)
for i in l2:
    l1.append(i)
for i in range(0,len(l1)):
    for j in range(0,len(l1)-1):
        if (l1[j]>l1[j+1]):
            temp=l1[j]
            l1[j]=l1[j+1]
            l1[j+1]=temp
print(l1)
for i in range(0,x1):
    print(l1[i], end=" ")
print()
for i in range(x1,x1+x2):
    print(l1[i], end=" ")
print()


    
                
    
