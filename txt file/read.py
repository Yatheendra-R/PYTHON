f=open("readexample.txt",'r')

#any one will work at a time in python idleshell

'''
x=f.readlines()   #list of string(whole txt)..first line will the string
print(x)
print(type(x))
print(len(x))    #len helps to find nuber of lines(number of string)
'''

'''
x1=f.read()            #string(whole txt) 
print(x1)
print(type(x1))
print(len(x1))        #also count the empty spaces and EOL till line before the end(if many lines present )
                      #when only 1 line present in count the empty spaces and also EOL of the line

'''

'''
print(f.read(6))      #read the given number of ch in the string of content
                      #including spcae
'''

'''
print(f.read(123))    #read the given number more than the content of ch in the string of content
                      #print the whole txt
'''

'''
print(f.read(6))      #print the content

print(f.read(7))      #print the content next line,print the content from wherev in left reading the txt
'''

'''
x2=f.readline()   #read(print) first line
print(x2)
print(type(x2))    #string
print(len(x2))     #include empty spaces
'''

'''
print(f.readline(5))  #read(print) first 5 ch of the first line
'''

'''
f.readline()           #read first line
f.readline()           #read second line 
print(f.readline())    #print the third line
'''

f.close()
