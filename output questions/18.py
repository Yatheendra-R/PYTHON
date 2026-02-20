def myfunc(n):
    n.append([4])
    p=n.copy()
    p[-1]=100
    return n.extend(p)
l=[1,2,3]
m=myfunc(l)
print(l,m)
