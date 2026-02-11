
l=[]
for i in range(3):
    l1=[]
    for j in range(1):
        l1.append(int(input("rno")))
        l1.append(input("name"))
        l1.append(int(input("total")))
    l.append(l1)

ln=[]
lm=[]
for  i in l:
    print(i[0],i[1],i[2],sep=",")
    ln.append(i[1])
    lm.append(i[2])
x1=max(lm)
print(x1)
ind=lm.index(x1)
print(ln[ind])

