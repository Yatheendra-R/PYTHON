def TUPLE(a):
    b=[]
    for i in range(len(a)):
        if a[i]%2!=0 and a[i]>10:
            b.append(a[i]%10*2)

        else:
            b.append(a[i]%5*3)
    return b
x=(4,17,24,9,81,8)
t=TUPLE(x)
print("Answer is:",t)
