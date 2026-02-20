def PRINT(s):
    a=b=""
    for i in s:
        if ord(i)>=65 and ord(i)<=90:
            a=a+i*2
        elif ord(i)>=97 and ord(i)<=122:
            b=2*i+b
    print("a=",a,"\nb=",b)
s="WelcoMe@BVM"
PRINT(s)
