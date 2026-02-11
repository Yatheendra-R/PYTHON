#swap main and sec dia
r=int(input('Enter the number of rows '))
print()
c=int(input('Enter the number of col '))
print()
l=[]
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input('Enter the number '))
        print()
        l1.append(x)
    l.append(l1)
print(l)
print()

#matrix
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()

#main
for i in range(r):
    for j in range(c):
        if i==j:
            print(l[i][j])
print()
#axial
for i in range(r):
    for j in range(c):
        if i+j==len(l)-1:
            print(l[i][j])
print()
l2=[]
#swap
for i in range(r):
    for j in range(c):
        if i==j or i+j==len(l)-1:
            l[i][j],l[i][j+2]=l[i][j+2],l[i][j]
print(l)
