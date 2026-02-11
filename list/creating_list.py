#creating a list

#method 1
l1=[]
print(l1)
print()

#method 2
l2=list()
print(l2)
print()

#method 3
l3=[1,'asd',[2,3,4]]
print(l3)
print()

#method 4
l4=[]
for i in range(3):
    x=int(input('Enter the number: '))
    l4+=[x]
print(l4)
print()

#method 5
l5=[]
for i in range(3):
    x1=int(input('Enter the number: '))
    l5.append(x1)
print(l5)
print()

#method 6
l6=eval(input('Enter the list: '))
print(l6)
print()

#method 7
l7=[]
for i in range(3):
    l7.append(int(input('Enter the number: ')))
print(l7)
print()
