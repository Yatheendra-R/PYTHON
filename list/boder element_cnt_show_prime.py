#boder element_cnt_show_prime
l=[]
r=int(input('Enter the number of rows '))
c=int(input('Enter the number of col '))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input('Enter the elements: '))
        l1.append(x)
    l.append(l1)
print(l)
print()

for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print()

sp=0
l2=[]
cnt=0
for i in range(r):
    for j in range(c):
        if i==0 or j==0 or i==len(l)-1 or j==len(l)-1:
            if l[i][j]!=0 and l[i][j]!=1:
                if l[i][j] not in l2:
                    for k in range(2,l[i][j]):
                        if l[i][j]%k==0:
                            break
                    else:
                        cnt+=1
                        sp+=l[i][j]
                        l2.append(l[i][j])
print(l2)
print(cnt)
print()
print(sp)
print()
