l=[]
for i in range(0,int(input("Enter the number of element in the list: "))):
    l.append(int(input("Enter the number: ")))
cnt=0
for i in range(0,len(l)):
    for j in range(0,len(l)-1):
        if l[j]>l[j+1]:
            cnt+=1
            temp=l[j]
            l[j]=l[j+1]
            l[j+1]=temp
print(cnt)
