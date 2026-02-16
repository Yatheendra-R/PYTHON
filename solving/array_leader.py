l=[]
for i in range(0,int(input("Enter the number of element in the list: "))):
    l.append(int(input("Enter the number: ")))
l1=[]
for i in range(0,len(l)-1):
    fg=0
    for j in range(i+1,len(l)):
        if (l[i]>=l[j]):
            pass
        else:
            fg=1
    if (fg==0):
        l1.append(l[i])
l1.append(l[len(l)-1])
print(l1)
