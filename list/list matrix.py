#nested list
'''l=[]
x=int(input('Enter the number of nested list:'))
y=int(input ('Enter the number of elements in the nested list:'))
for i in range(x):
    l1=[]
    for j in range(y):
        n1=int(input ('Enter the elements in the nested list:'))
        l1.append(n1)
    l.append(l1)
print(l)'''
#list
'''l=[]
n=int(input('Enter the number of elemnts in the list'))
for i in range(n):
    l.append(n)
print(l)'''
#matrix
'''l=[]
r=int(input('Enter the number of rows:'))
c=int(input('Enter the number of col:'))
for i in range(r):
    l1=[]
    for j in range(c):
        n1=int(input ('Enter the elements in the nested list:'))
        l1.append(n1)
    l.append(l1)
print(l)
for i in range(r):
        for j in range(c):
            print(l[i][j],end=" ")
        print()'''
#border elements
'''l=[]
r=int(input('Enter the number of rows:'))
c=int(input('Enter the number of col:'))
for i in range(r):
    l1=[]
    for j in range(c):
        n1=int(input ('Enter the elements in the nested list:'))
        l1.append(n1)
    l.append(l1)
print(l)
for i in range(len(l)):
        for j in range(len(l)):
            if i==0 or i==len(l)-1 or j==len(l)-1 or j==0:
                print(l[i][j],end=" ")
            else:
                print('  ',end='')
        print()'''
#sum of border elements
'''l=[]
r=int(input('Enter the number of rows:'))
c=int(input('Enter the number of col:'))
for i in range(r):
    l1=[]
    for j in range(c):
        n1=int(input ('Enter the elements in the nested list:'))
        l1.append(n1)
    l.append(l1)
print(l)
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==0 or j==0 or i==len(l)-1 or j==len(l)-1:
            s+=l[i][j]
            print(l[i][j],end=' ')
        else:
            print(' ',end=' ')
    print( )
print("sum of border elements",s)'''
#main diagonal                                                              
'''l=[]                                                                                                            
r=int(input('Enter the number of rows:'))                              
c=int(input('Enter the number of col:'))                           
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the no.of elements:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            print(l[i][j])
        else:
            print(' ',end=' ')
    print()'''
#axial diagonal
'''l=[]                                                               
r=int(input('Enter the number of rows:'))                              
c=int(input('Enter the number of col:'))                           
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
print(len(l))
for i in range(len(l)):
            print(l[i][(len(l)-1)-i])'''
#sum of main diagnol
'''l=[]
r=int(input('Enter the number of rows:'))
c=int(input("Enter the number of cols:"))
for i in range (r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the number:"))
        l1.append(c)
    l.append(l1)
print(l)
print("original matrix")
for i in range (r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("sum of main...")
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            print(l[i][j],end=" ")
            s+=l[i][j]
        else:
            print(" ",end=" ")
    print( )
print("sum of main diagnol",s)'''
#sum of axial diagnol
'''l=[]
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of cols:"))
for i in range (r):
    l1=[]
    for j in range (c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
      for j in range (c):
          print(l[i][j],end=" ")
      print( )
s=0
for i in range( len(l)):
          if(l[i][(len(l)-1)-i]):
              s+=(l[i][(len(l)-1)-i])
              print(l[i][(len(l)-1)-i])
print(s)'''
#sum of all the elements present in matrix
'''l=[]
r=int(input('Enter the number of rows:'))
c=int(input('Enter the number of col:'))
for i in range(r):
    l1=[]
    for j in range(c):
        n1=int(input ('Enter the elements in the nested list:'))
        l1.append(n1)
    l.append(l1)
s=0
print(l)
for i in range(r):
    for j in range(c):
        if l[i][j]:
            s+=l[i][j]
        print(l[i][j],end=" ")
    print( )
print(s)'''
#diplay each row
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=" ")
    print( )
print("*********************************")
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j])
    if i!=len(l)-1:
        print('next row')'''
#display 1,2 and 3 row
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
print("first row")
for i in range(len(l)):
    print(l[len(l)-len(l)][(len(l)-3)+i])
print("second row")
for i in range(len(l)):
    print(l[len(l)+1-len(l)][(len(l)-3)+i])
print("third row")
for i in range(len(l)):
    print(l[len(l)+2-len(l)][(len(l)-3)+i])'''
#display the sum of each row
'''l=[]
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        n=int(input('Enter the number:'))
        l1.append(n)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("**************")
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        s+=l[i][j]
        print(l[i][j])
    print("sum of each row is",s)
    if i!=len(l)-1:
            print('next row')
    else:
        print("has reached end of the row of the matrix")'''
#display the sum of first, second and third row
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
s=0
print("first row")
for i in range(len(l)):
    s+=l[len(l)-len(l)][(len(l)-3)+i]
    print(l[len(l)-len(l)][(len(l)-3)+i])
print("sum of first row",s)
s=0
print("second row")
for i in range(len(l)):
    s+=l[len(l)+1-len(l)][(len(l)-3)+i]
    print(l[len(l)+1-len(l)][(len(l)-3)+i])
print("sum of second row",s)
s=0
print("third row")
for i in range(len(l)):
    s+=l[len(l)+2-len(l)][(len(l)-3)+i]
    print(l[len(l)+2-len(l)][(len(l)-3)+i])
print("sum of third row",s)'''
#diplay each col
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(len(l)):
    for j in range(len(l)):
        print(l[i][j],end=" ")
    print( )
print("*********************************")
for i in range(len(l)):
    for j in range(len(l)):
        print(l[j][i])
    if i!=len(l)-1:
        print('next col')'''
#sum of each row
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
for i in range (c):
    s=0
    for j in range (r):
        s+=l[i][j]
    print(s)'''
#display 1,2 and 3 col
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
print("first col")
for i in range(len(l)):
    print(l[(len(l)-3)+i][len(l)-len(l)])
print("next col")
for i in range(len(l)):
    print(l[(len(l)-3)+i][len(l)+1-len(l)])
print("next col")
for i in range(len(l)):
    print(l[(len(l)-3)+i][len(l)+2-len(l)])'''
#display the sum of each col
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
print("***************")
for i in range(len(l)):
    s=0
    for j in range(len(l)):
        s+=l[j][i]
        print(l[j][i])
    print("sum ofcol",s)
    if i!=len(l)-1:
        print("next col")'''
#diaplay the sum of 1,2 and 3 col
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
print("frst col")
s=0
for i in range(len(l)):
    print(l[(len(l)-3)+i][len(l)-len(l)])
    s+=(l[(len(l)-3)+i][len(l)-len(l)])
print("sum of first col:",s)
print("second col")
s=0
for i in range(len(l)):
    print(l[(len(l)-3)+i][len(l)+1-len(l)])
    s+=(l[(len(l)-3)+i][len(l)+1-len(l)])
print("sum of second col:",s)
print('third col') 
s=0
for i in range(len(l)):
    print(l[(len(l)-3)+i][len(l)+2-len(l)])
    s+=(l[(len(l)-3)+i][len(l)+2-len(l)])
print("sum of third col:",s)'''
# sum of each the coll
'''l=[]
r=int(input("ENTER THE NUMBER OF ROWS:"))
c=int(input("ENTER THE NUMBER OF COLS:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("ENTER THE NUMBERS:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=' ')
    print( )
for i in range (c):
    s=0
    for j in range (r):
        s+=l[j][i]
    print(s)'''
#upper triangle
'''l=[]
c=int(input("Enter the number of row:"))
r=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("upper triangle")
for i in range(len(l)):
    for j in range(len(l)):
        if i>=j:
            print(l[i][j],end=" ")
    print( )'''
#lower triagle
'''l=[]
c=int(input("Enter the number of row:"))
r=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("lower triangle")
for i in range(len(l)):
    for j in range(len(l)):
        if i<=j:
            print(l[i][j],end=" ")
    print( )'''            
#upper triangle display and sum
'''l=[]
c=int(input("Enter the number of row:"))
r=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("upper triangle")
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i>=j:
            s+=l[i][j]
            print(l[i][j],end=" ")
    print( )
print("sum of upper triangle is",s)'''            
#lower triangle display and sum
'''l=[]
c=int(input("Enter the number of row:"))
r=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("lower triangle")
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i<=j:
            s+=l[i][j]
            print(l[i][j],end=" ")
        else:
            print(" ",end=" ")
    print( )
print("sum of lower triangle is",s)'''
#bubble sort(assending)
'''l=[]
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=(input("enter the words:"))
        l1.append(x)
    l.append(l1)
print(l)
print("sorting")
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[i]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''
#bubble sort(desending)
'''l=[]
r=int(input("Enter the number of rows:"))
c=int(input("Enter the number of cols:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=(input("enter the words:"))
        l1.append(x)
    l.append(l1)
print(l)
print("sorting")
for i in range(len(l)-1):
    for j in range(len(l)-1-i):
        if l[i]<l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
print(l)
'''
#print "0" in place of free space(upper triangle)
'''l=[]
r=int(input("Enter the number row:"))
c=int(input("Enter the number of col:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("upper triangle")
for i in range(len(l)):
    for j in range(len(l)):
        if i>=j:
            print(l[i][j],end=" ")
        else:
            print("0",end=" ")
    print( )'''
#print "0" in place of free space(lower triangle)
'''l=[]
r=int(input("Enter the number row:"))
c=int(input("Enter the number of col:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
print("lower triangle")
for i in range(len(l)):
    for j in range(len(l)):
        if i<=j:
            print(l[i][j],end=" ")
        else:
            print("0",end=" ")
    print( )'''
#perfect number(cont and verify)
'''l=[]
cnt=0
x=int(input("Enter the number of elements:"))
for i in range(x):
    y=int(input("Enter the elements:"))
    l.append(y)
    s=0
    for j in range(1,y):
        if(y%j==0):
            s+=j
    if(s==y):
        cnt+=1
        print(y,"is a perfect number")
    else:
        print("There is no perfect number")
print(l)
print(cnt,"number of perfecy number")'''
#mean of main diagnol
'''l=[]
r=int(input("Enter the number row:"))
c=int(input("Enter the number of col:"))
for i in range(r):
    l1=[]
    for j in range(c):
        x=int(input("Enter the numbers:"))
        l1.append(x)
    l.append(l1)
print(l)
for i in range(r):
    for j in range(c):
        print(l[i][j],end=" ")
    print( )
s=0
for i in range(len(l)):
    for j in range(len(l)):
        if i==j:
            print(l[i][j],end=" ")
            s+=l[i][j]
          
        else:
            print(" ",end=" ")
    print( )
z=len(l)
print(z)
print("sum",s)
mean=s/z
print("mean is",mean)'''
#even,odd, prime in a list(cnt and show and sum)
#mean of axial diagnol
#swap diagnols, cols and row
#swap alternate col and row
#transpose of list
#diplay index position of even no. in matrix
#even,odd,prime in upper and lower triangle,col,row,main and axial diagnol,boder elements.
#print ** in empty space of border elements
l1=[]
for i in range(5):
    l2=[]
    for j in range(5):
        print('REMINDER ***DO NOT REPEAT THE NUMBER***')
        print()
        a2=int(input ('Enter the number:'))
        print()
        l2.append(a2)
    l1.append(l2)
    print('Entered number are ',l1)
    print()
