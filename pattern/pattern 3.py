
ch="A"      
for k in range (1,3*2+1):
   if k%2==1:
      print("1")
      break
for k in range (1,3*2+1):

   if k%2==0:
    print("1",end=" ")
    for j in range(1,k):
        print("0",end=" ")
    
    print(ch)
    ch=chr(ord(ch)+1)
   

    
    
   

