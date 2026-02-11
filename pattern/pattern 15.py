#output pattern 16
'''
y 
y a 
y a t 
y a t h 
y a t h i 
'''

s=input("Enter a name")
for i in range(len(s)+1):
    for j in range(i):
        print(s[j],end=" ")
    print()
