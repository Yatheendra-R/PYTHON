import csv
with open("nested.csv","w",newline="")as f:
    l=[]
    for i in range(2):
        l1=[]
        for j in range(2):
            x=int(input("Enter the numbers"))
            l1.append(x)
        l.append(l1)
    x=csv.writer(f)
    x.writerows(l)
