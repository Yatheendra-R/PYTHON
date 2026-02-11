'''
   1
  12
 123
1234
'''
for i in range (1,5):
    for j in range(1,5-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print( ) 
