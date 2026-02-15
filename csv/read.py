import csv
with open('writing.csv', 'r') as file:
    reader = csv.reader(file)
    print(reader)
    
    for row in reader:
        print(row)
