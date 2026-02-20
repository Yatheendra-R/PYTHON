#output 1
t=["Hi!","AnnUaLEXAm","Good day"]
tt =[]
for i in t:
    if i.isalpha():
        f=""
        for j in i:
            if j.isupper():
                f+= chr(ord(j) + 34)
            else:
                f+= chr(ord(j) - 32)
        tt.append(f)
    else:
        tt.append ( i* 2)

print(tt)
