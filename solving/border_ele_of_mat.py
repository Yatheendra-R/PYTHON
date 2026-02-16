r=int(input("Enter the row: "))
c=int(input("Enter the col: "))
l=[]
for i in range(r):
    l1=[]
    for j in range(c):
        l1.append(int(input("Enter the number: ")))
    l.append(l1)
for i in range(len(l)):
    for j in range(len(l[0])):
        print(l[i][j],end=" ")
    print()
for i in range(len(l)):
    for j in range(len(l[0])):
        if (i==0 or j==0 or i==r-1 or j==c-1):
            print(l[i][j],end=" ")
    
