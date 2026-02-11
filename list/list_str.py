'''l=[]
x1=int(input("Enter the number of ppl:"))
for i in range(x1):
    rno=int(input("rno"))
    name=input("name")
    t=()
    t+=(rno,)
    t+=(name,)
    print(type(t))
    l.append(t)
print(type(l))
print(l)
'''
t=[(1, 'ab'), (2, 'bc')]
x=[]
x1=""
for i in t:
    x.append(i[1])
    x1+=i[1]
    x1+=","

x1=x1[:-1]
    
    

print(x)
print(x1)

