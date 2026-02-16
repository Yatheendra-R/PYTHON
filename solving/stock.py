#l=[100,180,260,310,40,535,695]
l=[4,2,2,2,4]
"""
for i in range(int(input("Enter the number of elements in list: "))):
    l.append(int(input("Enter the number: ")))"""
l.append(0)

max_pr=0
buy_pr=0
sel_pr=0
for i in range(len(l)-1):
    if (l[i]<l[i+1]):
        #buy_pr=l[i]
        sel_pr+=(l[i+1]-l[i])
    if (l[i]>l[i+1]):
        #sel_pr=l[i]
        max_pr+=(sel_pr)
        sel_pr=0

print(max_pr)
