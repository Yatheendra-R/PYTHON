#find the index posi. of each element
l=[]
x=int(input('Enter the number of elements: '))
for i in range(x):
    x1=int(input("Enter the number: "))
    l.append(x1)
print(l)
print()

for i in range(len(l)):
    print('Index position of number ',l[i],' is ',i)
    print()
