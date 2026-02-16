l=[]
x=int(input("Enter the number of element in the list: "))
for i in range(x):
    num=int(input("Enter the number: "))
    l.append(num)
fg=0
for i in l:
    if i<0:
        fg=1
if (fg==0):
    print(l)
    print(sum(l))
else:
    max_sum=0
    ind1=0
    ind2=0
    for i in range(0,len(l)):
        suming=0
        for j in range(i,len(l)):
            suming+=l[j]
            if (suming>max_sum):
                max_sum=suming
                ind1=i
                ind2=j
    print(ind1,ind2,max_sum) 
    print(l)
    for i in range(ind1,(ind2+1)):
        print(l[i],end=", ")
        print()
    
