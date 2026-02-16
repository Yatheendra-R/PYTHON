

l=[]
x=int(input("Enter the number of element in the list: "))
for i in range(0,x):
    l.append(int(input("Entre the number: ")))
print(l)
l.sort()
print(l)
start=l[0]
fg=0
for i in l:
    if (start!=i):
        fg=1
        print("Missing element b/w ",l[0]," and ",l[len(l)-1], " is: ",start)
        break
    start+=1
if (len(l)==1):
        print("Only ",l[0]," is present so missing element is: ",l[len(l)-1]+1)

    
elif (fg==0):
    print("Everything is present in b/w ",l[0]," and ",l[len(l)-1]," so missing element is: ",l[len(l)-1]+1)
