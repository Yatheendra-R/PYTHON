#l=[2,1,5,3,1,0,2]
#l=[3,0,2,0,4]
#l=[1,2,3,4]
#l=[2,1,5,3,1,0,4]
#l=[0,1,0,2,1,0,1,3,2,1,2,1]
l=[1,7,5]

l1=[]
for i in range(len(l)):
    l2=[]
    for j in range(len(l)):
        l2.append(1)
    l1.append(l2)
#print(l1)

for i in range(len(l)):
    end_ind=len(l)-1
    curr_val=l[i]
    
    while True:
        if curr_val==0:
            break
        else:
            l1[len(l)-curr_val][i]=0
            
            curr_val-=1
            end_ind=-1
"""for i in l1:
    print(i)
print()"""
for i in range(len(l1)):
    for j in range(len(l1[0])):
        if l1[i][j]==1:
            l1[i][j]=0
        elif( l1[i][j]==0):
            break
"""
for i in l1:
    print(i)
"""
#print()
for i in range(len(l1)):
    for j in range(len(l1[0])-1,-1,-1):
        if l1[i][j]==1:
            l1[i][j]=0
        elif( l1[i][j]==0):
            break
"""
for i in l1:
    print(i)"""


cnt=0
for i in range(len(l1)):
    for j in range(len(l1[0])):
        if l1[i][j]==1:
            cnt+=1
print(cnt)
    
    
