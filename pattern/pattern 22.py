#pattern 1
'''
output:
1
12
123
1234
'''
'''for i in range (1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print( )'''
#pattern 2
'''
1
22
333
4444
'''
'''for i in range(1,5):
    for j in range(1,i+1):
        print(i,end=' ')
    print()'''
#pattern 3
'''
   1
  12
 123
1234
'''
'''for i in range (1,5):
    for j in range(0,4-i):
        print(" ",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print( )'''
#pattern 4
'''
a
ab
abc
abcd

'''
'''for i in range(1,5):
    ch="a"
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print( )'''
#pattern 4.1
'''
a b c d 
a b c 
a b 
a 
'''
'''
for i in range(1,5):
    ch="a"
    for j in range(1,6-i):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print( )
'''
#pattern
'''
1d
12c
123b
1234a
'''
'''
ch="d"
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=" ")
    print(ch,end=" ")
    ch=chr(ord(ch)-1)
    
    print( )
    '''
#pattern 5
'''
*
**
***
****
'''

'''for i in range(1,5):
    for j in range(1,i+1):
        print('*',end=" ")
    print()'''

#pattern 6
'''
@@@@@a
@@@@b
@@@c
@@d
@e
'''
'''ch="a"
for i in range(1,6):
    for j in range(1,7-i):
        print("@",end=" ")
    print(ch,end=" ")
    ch=chr(ord(ch)+1)
    print()'''
#patter 7
'''
1#
1*2*
1#2#3#
1*2*3*4*
'''
'''
for i in range(1,5):
    for j in range(1,i+1):
            if i%2==0:
                print(j,end="*")
            else:
                print(j,end="#")
    print( )
'''
#pattern 8
'''
1a
1b2b
1c2c3c
1d2d3d4d
'''
'''ch="a"
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=ch)
    ch=chr(ord(ch)+1)
    print( )
'''
#pattern 9
'''
1a
1b2c
1d2e3f
1g2h3i4j
'''
'''ch="a"
for i in range(1,5):
    for j in range(1,i+1):
        print(j,end=ch)
        ch=chr(ord(ch)+1)
    print( )'''
#pattern 10
'''
10 
20 30 
40 50 60 
70 80 90 100
'''
'''int=10
for i in range(1,5):
    for j in range(1,i+1):
        print(int,end=' ')
        int+=10
    print()'''
#pattern 11
'''
10
10 20
10 20 30
10 20 30 40
'''

'''for i in range(1,5):
    int=10
    for j in range(1,i+1):
        print(int,end=' ')
        int+=10
    print()'''
#pattern 12
'''
a 
b c 
d e f 
g h i j
'''
'''ch="a"
for i in range(1,5):
  for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
    print( )'''
# pattern 13
'''
   1 
  1 2 
 1 2 3 
1 2 3 4 
'''
'''
for i in range (1,5):
    for j in range(0,4-i):
        print("",end=" ")
    for k in range(1,i+1):
        print(k,end=" ")
    print( )'''

#pattern 14
'''
@ a 
@ @ b 
@ @ @ c 
@ @ @ @ d 
@ @ @ @ @ e
'''
'''ch="a"
for i in range(1,6):
    for j in range(1,i+1):
        print("@",end=" ")
    print(ch,end=" ")
    ch=chr(ord(ch)+1)
    print()'''
#pattern 15
'''
1#
2*2*
3#3#3#
4*4*4*4*
'''
'''
ints=1
for i in range(1,5):
    for j in range(1,i+1):
        if i%2==0:
            print(ints,end="*")
        else:
            print(ints,end="#")
    ints+=1
    print( )
'''
#pattern
'''
4*4*4*4*
3#3#3#
2*2*
1#
'''
'''
ints=4
for i in range(1,5):
    for j in range(1,6-i):
        if i%2==0:
            print(ints,end="#")
        else:
            print(ints,end="*")
    ints-=1
    print( )
    '''
#pattern
'''
4#4#4#4#
3*3*3*
2#2#
1*
'''
'''
ints=4
for i in range(1,5):
    for j in range(1,6-i):
        if i%2==0:
            print(ints,end="*")
        else:
            print(ints,end="#")
    ints-=1
    print( )
'''

#pattern
'''
4*4*4*4*
3#3#3#
2*2*
1#
'''
'''
ints=4
for i in range(1,5):
    for j in range(1,6-i):
        if i %2==0:
            print(ints,end="#")
        else:
            print(ints,end="*")
    ints-=1
    print( )
'''

#pattern
'''
4#4*4#4*4#4*4#4*
3#3*3#3*3#3*
2#2*2#2*
1#1*
'''
'''
ints=4
for i in range(1,5):
    for j in range(1,6-i):
        print(ints,end="#")
        print(ints,end="*")
    ints-=1
    print( )
    '''

#pattern 16
'''
1a
1a2b
1a2b3c
1a2b3c4d
'''
'''for i in range(1,5):
    ch="a"
    for j in range(1,i+1):
        print(j,end=ch)
        ch=chr(ord(ch)+1)
    print( )'''
#pattern 17
'''
a 
b b 
c c c 
d d d d
'''
'''
ch="a"
for i in range(1,5):
    for j in range(1,i+1):
        print(ch,end=' ')
    ch=chr(ord(ch)+1)
    print( )
'''
#pattern 18
'''
1
23
456
78910
'''
'''
ints=1
for i in range(1,5):
    for j in range(1,i+1):
        print(ints,end=" ")
        ints+=1
    print( )
    '''
#pattern 19
'''
10
20 20
30 30 30
40 40 40 40
'''
'''
ints=10
for i in range(1,5):
    for j in range(1,i+1):
        print(ints,end=" ")
    ints+=10
    print( )
'''
#pattern 20
'''
5 4 3 2 1 -15
4 3 2 1 -10
3 2 1 -6
2 1 -3
1 -1
'''

'''
for i in range(5,0,-1):
    s=0
    for j in range(i,0,-1):
        print(j,end=" ")
        s+=j
    print("-",s)
'''
#pattern 21
'''
a65
ab66
abc67
abcd68
abcde69
'''
'''
num=65
for i in range(1,6):
    ch="a"
    for j in range(1,i+1):
        print(ch,end="")
        ch=chr(ord(ch)+1)
    print(num)
    num+=1
'''
#pattern 22
'''
1
10A
1000B
100000C
'''
print('1')
for i in range (3):
    print('1',' 0 '*((2*i)+1),chr(65+i))
#pattern 21
#pattern 21
#pattern 21
#pattern 21
#pattern 21
#pattern 21

