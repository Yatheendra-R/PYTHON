#series
n=3
x=1
s=0
p=1
de=2
for i in range(1,n+1):
   a=x**p
   p+=2
   f=0
   d=1

   for j in range(de):
       f+=1
       d*=f
       if j==de-1:
            de+=2
   if i%2==0:
       s=s-(a/d)
   else:
       s=s+(a/d)
    
print(s)


