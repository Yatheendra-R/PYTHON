'''
a 
b b 
c c c 
d d d d
'''

ch="a"
for i in range(1,5):
    for j in range(1,i+1):
        print(ch,end=' ')
    ch=chr(ord(ch)+1)
    print( )
