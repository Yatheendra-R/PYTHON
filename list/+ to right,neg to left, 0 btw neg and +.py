#+ to right,neg to left, 0 btw neg and +
l=[1,-6,0,-5,18-6,-20,12,36]
l1=[]
for i in range(len(l)):
    if l[i]<0:
        l1.append(l[i])
        
for i in range(len(l)):
    if l[i]==0:
        l1.append(l[i])

for i in range(len(l)):
    if l[i]>0:
        l1.append(l[i])

print(l1)
