L=[1,3,4,4,5,2,1,4,3,1]
d=dict()
L.remove(4)
for i in range(len(L)):
    if L[i]not in L[:i]:
        d[L[i]]=L.count(L[i])
print(d)
