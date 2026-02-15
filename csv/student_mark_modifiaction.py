import csv,os
'''
with open("studentmarks.csv","w",newline="") as f:
    w=csv.writer(f)
    w.writerow(["Rollnumber","Name","Total"])
    for i in range(int(input("Enter number of student: "))):
        rol=int(input("Enter the rollnumber: "))
        nam=input("Enter the name: ")
        tot=int(input("Enter the total: "))
        w.writerow([rol,nam,tot])
        
with open("studentmarks.csv","r") as f1:
    with open("orgstudentmarks.csv","w") as f2:
    
        w1=csv.reader(f1)
        w2=csv.writer(f2)
        c=0
        for i in w1:
            if c>0:
                w2.writerow([i[0],i[1],int(i[2])+30])
                
            elif c==0:
                w2.writerow(i)
                c=1
        
'''
os.remove("studentmarks.csv")
os.rename("orgstudentmarks.csv,studentmarks.csv")





