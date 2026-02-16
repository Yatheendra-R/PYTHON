x=int(input("Enter the number of element in the list: "))
l=[]
for i in range(x):
    num=int(input("Enter the number: "))
    l.append(num)
l1=[]
suming=0
for i in l:
    for j in l:
        if j!=i:
            suming=i+j
            if suming in l:
                l4=[j,i]
                if l4 not in l1:
                    l1.append([i,j])
                    print(i," + ",j," = ",suming)
print("number of triplet: ",len(l1))               
if (len(l1)==0):
    print("No such triplet exits")
    
"""
print(l1)     
for i in l1:
    l2=[i[1],i[0]]
    if l2 in l1:
        i[0]="D"
for i in l1:
    if (type(i[0])==int):
        print(i[0]," + ",i[1] ," = ",i[0]+i[1])
"""      
