#prime no
l=[]
x=int(input('Enter the number of element: '))
for i in range(x):
    x1=int(input('Enter the no. '))
    l.append(x1)
print(l)
c=0
l1=[]
for i in range(len(l)):
    for j in range(2,l[i]):
        if l[i]%j==0:
            break
    else:
        c+=1
        l1.append(l[i])
print(c,' number of prime no.')
print()
print('prime no. are ',l1)
            
