#no. of odd and even num
l=[]
x=int(input('Enter the number of elements: '))
for i in range(x):
    x1=int(input("Enter the no. "))
    l.append(x1)
print(l)
print()

ne=0
no=0

for i in range(len(l)):
    if l[i]%2==0:
        ne+=1
    else:
        no+=1
print('Number of even no. ',ne)
print()
print('Number of odd no. ',no)
print()
