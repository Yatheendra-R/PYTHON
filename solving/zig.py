r=int(input("Enter the row: "))
c=int(input("Enter the col: "))
l=[]
for i in range(r):
    l1=[]
    for j in range(c):
        l1.append(int(input("Enter the number: ")))
    l.append(l1)
dir_l=[1,2,3,4]
ind=0
cond_dir=r*c
sum_cnt=0
i=0
j=0

l2=[]
print(l[i][j])
l2.append(l[i][j])

""""
1   2   3   4
5  6   7   8
9  10  11  12
13  14 15 16
"""



while (cond_dir!=sum_cnt):
    if (dir_l[ind]==1):
        if(j==c-1):
            ind+=1
        elif (l[i][j]==-1):
            ind+=1
        else:
            j+=1
            print(l[i][j])
            l2.append(l[i][j])
            l[i][j]==-1
            ind+=1
            sum_cnt+=1
    elif(dir_l[ind]==2):
        while True:
            
            if (j==0 or i==r-1):
                ind+=1
                break
            elif (l[i][j]==-1):
                ind+=1
                break
            else:
                j-=1
                i+=1
                print(l[i][j])
                l2.append(l[i][j])
                l[i][j]=-1
                sum_cnt+=1
                
    elif (dir_l[ind]==3):
            if(i==r-1):

                ind+=1
            elif (l[i][j]==-1):
                ind+=1
                
            else:
                sum_cnt+=1
                i+=1
                print(l[i][j])
                l2.append(l[i][j])
                l[i][j]=-1
                ind+=1
    elif (dir_l[ind]==4):
        while True:
            if(j==c-1 or i==0):
                ind=1
                break
                
            elif (l[i][j]==-1):
                ind=1
                break
            else:
                
                i-=1
                j+=1
            
                print(i,j," ",l[i][j])
                l2.append(l[i][j])
                l[i][j]=-1
                sum_cnt+=1
                if (i==0):
                    ind=0
                    break
print()
print(sum_cnt)
print(l2)
print(l)
            
            
        
            
            
            
        
