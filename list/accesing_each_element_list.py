#accesing each element in the list
l=[]
x=int(input('Enter the number elements '))
for i in range(x):
    x1=int(input('Enter the no. '))
    l.append(x1)
print(l)
print()

for i in range(len(l)):
    print(l[i])
    print()
