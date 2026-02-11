#neg left,pos right, zero del
l=[1,-6,0,-5,18-6,-20,12,36]
l1=[]
l2=list(l)

for i in range(len(l)):
    if l[i]==0:
        l2.remove(l[i])
print(l2,' Removing zero from original list')
print()

for i in range(len(l)):
    if l[i]<0:
        l1.append(l[i])

for i in range(len(l)):
    if l[i]>0:
        l1.append(l[i])
print(l1)
