l=[]
x=int(input("Enter the number of element in the list: "))
for i in range(0,x):
    l.append(int(input("Enter the number: ")))
l1=l.copy()
l1.sort()
print(l)
print(l1)
l3=[]
leng=len(l1)
end_range=len(l1)//2
for i in range(0,end_range):

    l3.append(l1[leng-1-i])
    l3.append(l1[i])
if (len(l1)%2==0):
    print(l3)
else:
    #l=[1,2,3,4,5,6,7]
    l3.append(l1[(len(l1)//2)])
    print(l3)





    
