#bubble sort of the nested list with the first element of the list
l=[]

c=int(input("Enter the no. of elements"))
r=int(input("Enter the no. of elements"))
for i in range(c):
    l1=[]
    for j in range(r):
        x=int(input("ELEMENTS"))
        l1.append(x)
    l.append(l1)
print(l)
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j][0]>l[j+1][0]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

