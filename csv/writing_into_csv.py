import csv
with open("writing.csv","w",newline='') as f:
    x=csv.writer(f)

    a="yes"
    while a=="yes":
        no=int(input("Enter the number of the employee: "))
        na=input("Enter vthe name of the employee: ")
        sa=int(input("Enter the salary name: "))
        x.writerow([no,na,sa])
        a=input("Do you want to add more(yes/no)? ").lower()
        
