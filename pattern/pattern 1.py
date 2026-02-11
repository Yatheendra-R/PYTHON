#pattern 1
'''
    5
   45
  345
 2345
12345
'''

for j in range(1,6):
    for i in range(1,6-j):
        print(" ",end=" ")
    ints=5
    for k in range(1,1+j):
        print(ints,end=" ")
        ints-=1 
    print()

s="python string fun"
while True :
    if s[0]==chr(ord('p')+32):
        s=s[3:].upper()
    elif s[-1]=='n':
        s=s[:2].lower()
    else:
        break
print(s)
