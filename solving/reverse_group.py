l=[]
for i in range(int(input("Enter the number of elements in the list: "))):
    l.append(int(input("Enter the number: ")))
k=int(input("Enter the key: "))
l1=[]
if k>len(l):
    l.reverse()
    print(l)
else:
    for i in range(k-1,-1,-1):
        l1.append(l[i])
    for i in range(len(l)-1,k-1,-1):
        l1.append(l[i])
    print(l1)

