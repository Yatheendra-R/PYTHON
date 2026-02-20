def u(s):
    for i in range(len(s)):
        if ord(s[i])>=65 and ord(s[i])<=70:
            print(chr(ord(s[i])+3),end="")
        elif ord(s[i])>=70 and ord(s[i])<=80:
            print(chr(ord(s[i])-3),end="")
        else: 
            print(chr(ord(s[i])+2),end="")
s="MARI"
print("us:",end="")
u(s)
