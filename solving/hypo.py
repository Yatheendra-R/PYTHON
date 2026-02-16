l=[]
for i in range(int(input("Enter the number of elements in the list: "))):
    l.append(int(input("Enter the number: ")))
for i in range(0,len(l)):
    l[i]=l[i]**2
print(l)
cnt=0
l1=[]

for i in l:
 
    for j in l:
        sum_ab=i

        if i!=j:
            sum_ab+=j
            if sum_ab in l:
                
                l1.append([i,j])
                l2=[j,i]
                if l2 not in l1:
                    print(i," + ",j," = ",i+j)
                    cnt+=1

if(cnt==0):
    print("False")
