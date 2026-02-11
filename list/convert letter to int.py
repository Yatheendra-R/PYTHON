#convert letter to int
l=[]
x=int(input('Enter the number of elements: '))
for i in range(x):
    x1=input('Enter each letter ')
    l.append(x1)
print(l)
print()

for i in range(len(l)):
    x2=ord(l[i])
    print(l[i],' letter ',x2,' is ascii value')
