#axial diagonal
l=[]                                                               
r=int(input('Enter the number of rows:'))                              
c=int(input('Enter the number of col:'))                           
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        if i+j==len(l)-1:
            print(l[i][j])
        else:
            print(' ',end=" ")
