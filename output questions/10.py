def LIST(a):
    for i in range(len(a)):
        if a[i]//10>0 and a[i]%2==0:
            a[i]-=a[i]%10
        else:
            a[i]+=a[i]%10

x=[4,17,42,6,16]        
LIST(x)
print("Updated values:",end="")
for a in x:
    print(a,end="#")
