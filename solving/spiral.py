"""
1   2   3  5
4  5   6   5

7   8   9  6


1 5 9 13 14 15 16 12 8 4 3 2 1 6 10 11 7
"""
l_d=[1,2,3,4]
ind=0
z=l_d[ind]


row=int(input("Enter the row: "))
col=int(input("Enter the col: "))
break_cond=row*col
"""l=[]
for k in range(row):
    l1=[]
    for p in range(col):
        l1.append(int(input("Enter the number: ")))
    l.append(l1)"""
#l=[[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16],[17,18,19,20]]
#l=[[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15],[16,17,18,19,20]]
l=[[1,2,3,4,5,6],[7,8,9,10,11,12],[13,14,15,16,17,18],[19,20,21,22,23,24],[25,26,27,28,29,30]]
print(l)
l2=[]
i=0
j=0
l3=[-1,-1]
l4=[]
sum_val=0
while True:
    l2.append(l[i][j])
    l[i][j]=-1
    l3=[i,j]
    print(l2)

    if (l3 not in l4):
        sum_val+=1
        l4.append(l3)
        if ((j==0) and (i!=(row-1))):
            i+=1
        elif(z==2):
            print(z)
            break
        elif ((i==(row-1)) and (j!=col-1)):
            j+=1
        elif ((i==row-1) or (j==col-1) and (i!=0)):
            i-=1
        elif ((i==0)):
            j-=1
            if (j==0):
                break
        
        
    else:  
        break

i=0
j=1
run=0
print(l,z,sum_val)
print(l2)
while (sum_val!=break_cond):
          
        if(z==1):
            
           
            i+=1
                
            print("in 1",i,j)
            print(i,j)
            if (l[i][j]==-1):
                print("1=>-1:",i,j)
                i-=1
                z=2
            else:
                l2.append(l[i][j])
                l[i][j]=-1
                sum_val+=1
                print("1: ",l2," ",l)
        elif(z==2):
            j+=1
            print("in 2",i,j)
            if (l[i][j]==-1):
                j-=1
                z=3
            else:
                l2.append(l[i][j])
                l[i][j]=-1
                sum_val+=1
                print("2: ",l2," ",l)
        elif(z==3):
            i-=1
            print("in 3",i,j)
            if (l[i][j]==-1):
                i+=1
                z=4
            else:
                l2.append(l[i][j])
                l[i][j]=-1
                sum_val+=1
                print("3: ",l2," ",l)
        elif(z==4):
            j-=1
            if (l[i][j]==-1):
                j+=1
                z=1
            else:
                l2.append(l[i][j])
                l[i][j]=-1

                sum_val+=1
                print("4: ",l2," ",l)
        
print(i,j)
print(l)
print(sum_val)
print(l2)
"""
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16

1 5 9 13 14 15 16 12 8 4 3 2 6 10 11 7

1 2  3 4
5 6 7 8
9 10 11 12


1  5 9 10 11 12 8 4 3 2 6 7

1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
17 18 19 20


1    2    3     4      5
6   7    8     9     10
11  12   13   14    15
16  17   18   19   20


1 6 11 16 17 18 19 20 15 10 5 4 3 2 7 12 13 14 9 8

1    2    3     4      5    6
7    8     9     10   11  12
13   14    15   16  17   18
19   20   21    22   23  24
25  26   27    28   29   30

1  7   13  19 25  26  27 28 29 30 24  18 12 6 5 4 3 2 8 14 20 21 22 23 17 11 10 9 15 16 






"""
    


