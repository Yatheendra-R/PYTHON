import csv
with open("writings.csv","r") as f:
    l=csv.reader(f)

    for i in l:
        print(i)
