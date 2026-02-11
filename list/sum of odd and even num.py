#sum of odd and even num
l=[]
x=int(input('Enter the number of elements: '))
for i in range(x):
    x1=int(input("Enter the no. "))
    l.append(x1)
print(l)
print()

se=0
so=0

for i in range(len(l)):
    if l[i]%2==0:
        se+=l[i]
    else:
        so+=l[i]
print('Number of even no. ',se)
print()
print('Number of odd no. ',so)
print()

