#odd add 5 and even multi 2 ,element
l=[]
x=int(input('Enter the number of elements: '))
for i in range(x):
    x1=int(input('Enter the number: '))
    l.append(x1)
print(l)
print()

for i in range(len(l)):
    if l[i]%2==0:
        l[i]*=2
    else:
        l[i]+=5
print(l)
print()

#or
'''
11=[]
for i in range(len(l)):
    if l[i]%2==0:
        x2=l[i]*2
        l1.append(x2)
    else:
        x3=l[i]+5
        l1.append(x3)
        
print(l1)
print()
'''
