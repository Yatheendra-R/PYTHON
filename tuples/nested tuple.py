'''t=()
for i in range(3):
    t1=()
    for j in range(3):
        x=int(input("Enter the number "))
        t1+=(x,)
    t+=(t1,)
print(t)

t=()
for i in range(2):
        x=int(input("Enter the number"))
print(t)
print(type(t))
'''
l=[]
for i in range(3):
    l1=[]
    for j in range(2):
        l1.append(int(input("no")))
    l.append(l1)
print(l)    
