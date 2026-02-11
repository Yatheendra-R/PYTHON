#bubble sort 
l=[]
c=int(input("Enter the no. of elements"))
for i in range(c):
    x=int(input("ELEMENTS"))
    l.append(x)
print(l)
n=len(l)
for i in range(n):
    for j in range(n-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)

