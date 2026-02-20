#output 2
a,b=" Dc the bestt!",'Always'
k=a. split ("e")
for i in k:
    c=0
    for j in i:
        if j.isalnum():
            c +=1

    if c > 3 :
        a = a.replace(i,b)
    else:
        k.append("fine")

print(k)

print(a)
