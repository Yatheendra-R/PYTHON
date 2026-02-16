l=[4,2,5,7]
"""
for i in range(int(input("Enter the number of elements in list: "))):
    l.append(int(input("Enter the number: ")))"""
for i in range(0,len(l)):
    fg=0
    for j in range(i+1,len(l)):
        if (l[i]>l[j]):
            fg=1
    for j in range(i-1,-1,-1):
        if(l[i]<l[j]):
            fg=1
    if fg==0:
        print("Index: ",i," value: ",l[i])
