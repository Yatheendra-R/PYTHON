import csv
def add():
    with open("furniture.csv","a",newline="") as f1:
        x=int(input("Enter the number of material to be added"))
        header=["F_ld","Description","Material","Price","Stock"]
        w=csv.DictWriter(f1,header)
        for i in range(x):
            F_ld=int(input("Enter the f_ld number: "))
            Description=input("Enter the description")
            Material=input("Enter the material")
            Price=int(input("Enter the price"))
            Stock=int(input("Enter the stock left"))
            d={"F_ld":F_ld,"Description":Description,"Material":Material,"Price":Price,"Stock":Stock}
            w.writerow(d)
add()
