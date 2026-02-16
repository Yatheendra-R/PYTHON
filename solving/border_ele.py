"""
1   2   3  4
5  6   7  8
9   10  11  12
13  14  15  16


1 5 9 13 14 15 16 12 8 4 3 2 1 6 10 11 7
"""

    

row=int(input("Enter the row: "))
col=int(input("Enter the col: "))
break_cond=row*col
l=[]
for i in range(row):
    l1=[]
    for j in range(col):
        l1.append(int(input("Enter the number: ")))
    l.append(l1)
print(l)
l2=[]
i=0
j=0
l3=[-1,-1]
l4=[]
while True:
    l2.append(l[i][j])
    l3=[i,j]
    print(l2)
    
    
    if (l3 not in l4):
        l4.append(l3)
        if ((j==0) and (i!=(row-1))):
            i+=1
        elif ((i==(row-1)) and (j!=col-1)):
            j+=1
        elif ((i==row-1) or (j==col-1) and (i!=0)):
            i-=1
        elif ((i==0)):
            j-=1
            """if (j==0):
                break"""
    else:
        print("hi")
        break
    
print(i,j)  
    


