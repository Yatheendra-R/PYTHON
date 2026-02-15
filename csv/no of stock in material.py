import csv
def view():
    with open("furniture.csv","r") as f2:
        w=csv.DictReader(f2)
        c=0
        for i in w:
            print(i)
            print(i["Material"])
            if i["Material"].lower()=="teak":
                if int(i["Price"]) > 30000 and int(i["Price"])< 50000:
                    c+=int(i["Stock"])
    print("Toatal number of stock:",c)
view()

