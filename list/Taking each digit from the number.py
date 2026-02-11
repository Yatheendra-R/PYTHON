#Taking each digit from the number
l=[]
x= int(input("Enter the number: "))
s=0
Str=str(x)
#print(Str)
#print(len(Str))

for i in range(len(Str),0,-1):
    
    l.append(Str[i-1])
print(l)

