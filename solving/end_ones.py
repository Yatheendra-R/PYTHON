st=input("Enter the string(0/1): ")
max_ind=-1
for i in range(len(st)):
    if (st[i]=='1'):
        max_ind=i
print(max_ind)
