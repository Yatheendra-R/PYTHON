'''
a b c d 
a b c 
a b 
a 
'''
for i in range(1,5):
    ch="a"
    for j in range(1,6-i):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print()
