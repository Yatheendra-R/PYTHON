#nested list
l=[]
x=int(input('Enter the number of nested list:'))
y=int(input ('Enter the number of elements in the nested list:'))
for i in range(x):
    l1=[]
    for j in range(y):
        n1=int(input ('Enter the elements in the nested list:'))
        l1.append(n1)
    l.append(l1)
print(l)
