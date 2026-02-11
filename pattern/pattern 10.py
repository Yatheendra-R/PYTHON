'''
a a a a 
b b b 
c c 
d 
'''
ch="a"
for i in range(1,5):
    for j in range(1,6-i):
        print(ch,end=' ')
    ch=chr(ord(ch)+1)
    print( )
