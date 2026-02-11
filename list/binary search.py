#binary search

def binary_sort(l,a):
    l.sort()
    lo=0
    up=len(l)-1

    while lo<=up:
        mi=(lo+up)//2

        if l[mi]==a:
            return mi
        elif l[mi]>a:
            up=mi
        elif l[mi]<a:
            lo=mi

l=[]
x=int(input("Enter the number of element in the list: "))
print()
for i in range(x):
    x1=int(input("Enter the number: "))
    l.append(x1)
a=int(input("Enter the number to be searched: "))
x1=binary_sort(l,a)
print(a," is present in ",x1+1," this position")
