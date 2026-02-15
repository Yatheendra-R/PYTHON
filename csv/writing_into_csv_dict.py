import csv
with open("dictwriting.csv","w",newline='') as f:
    num=int(input("Enter the number of students: "))
    header=["rno","name","Mark"]
    w=csv.DictWriter(f,header)
    w.writeheader()
    for i in range(num):
        a=int(input("Roll number: "))
        b=input("Name: ")
        c=int(input("Enter the mark"))
        d={"rno":a,"name":b,"Mark":c}
        w.writerow(d)
