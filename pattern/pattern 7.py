'''
a
ab
abc
abcd
'''
for i in range(1,5):
    ch="a"
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
