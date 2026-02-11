#sorting a nested list
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

for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print()
for k in range(len(l)):
     for i in range(len(l[k])):
          for j in range(len(l[k])-i-1):
              if l[k][j] > l[k][j+1]:
                  l[k][j],l[k][j+1]=l[k][j+1],l[k][j]          
print(l)

