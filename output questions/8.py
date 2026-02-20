sums=0
dc1={}
dc1[1]=1
dc1['1']=2
dc1[1.0]=4
print(dc1)
for k in dc1:
    sums=sums+dc1[k]
    print(sums)
