import csv
with open("dictwriting.csv","r") as f1 ,open("modi.csv","w") as f2:
    x=csv.DictReader(f1)
    header=["Rno","name","mark"]
    z1=csv.DictWriter(f2,header)
    z1.writeheader()
    z=int(input("Enter the rollno: "))
    c=0
    for i in x:
        if int(i["rno"])==z:
            z1=int(input("Enter mark"))
            i["Mark"]=str(z1)
            c=1
            print(i)
            print(type(i))
            z1.writerows(i)

        else:
            z1.writerow(i)
        

                    

            
        
    if c==0:
        print("Entered the roll number is not present")
    
