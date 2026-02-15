import csv
with open("writings.csv","w",newline='') as f:
    x=csv.writer(f)
    l=[];
    a="yes"
    while a=="yes":
        no=int(input("Enter the employee id: "))
        na=input("Enter vthe name of the employee: ")
        sa=int(input("Enter the salary name: "))
        #x.writerow([no,na,sa])
        l1=[no,na,sa]
        a=input("Do you want to add more(yes/no)? ").lower()
        l.append(l1)
    x.writerows(l)
