#ascii value of each letter of the word
l=list(input("Enter a word"))
for i in range(len(l)):
       l[i]=str(l[i])
print(l)
print()

for i in range(len(l)):
    x2=ord(l[i])
    print(l[i],' letter ',x2,' is ascii value')
