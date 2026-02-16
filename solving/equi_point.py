l=[]
fg=0
for i in range(0,int(input("Enter the number of element in the list: "))):
    l.append(int(input("Enter the number: ")))
for i in range(1,len(l)-1):
    sum1=0
    sum2=0
    for j in range(0,i):
        sum1+=l[j]
    for k in range(i+1,len(l)):
        sum2+=l[k]
    if sum1==sum2:
        print("EQUI INDEX: ",i)
        print("sum is: ",sum1)
        fg=1
        break
if (fg==0):
    print("NO EQUI INDEX")
    
