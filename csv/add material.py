import csv
def create():
    with open("furniture.csv","w",newline="") as f:
        header=["F_ld","Description","Material","Price","Stock"]
        w=csv.DictWriter(f,header)
        w.writeheader()
        x=int(input("Enter the number material"))
        for i in range(x):
            F_ld=int(input("Enter the f_ld number: "))
            Description=input("Enter the description")
            Material=input("Enter the material")
            Price=int(input("Enter the price"))
            Stock=int(input("Enter the stock left"))
            d={"F_ld":F_ld,"Description":Description,"Material":Material,"Price":Price,"Stock":Stock}
            w.writerow(d)
            
            
            
        
        
        
    
create()
