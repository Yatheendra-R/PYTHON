#sorting a list
l=[1,-6,0,-5,18-6,-20,12,36]

for i in range(len(l)):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
