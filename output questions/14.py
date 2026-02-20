def ChangeVal(M,N): #m=l,n=4
    for i in range(4): #i=0,1,2,3
        if M[i]%5 == 0: #true
            M[i]//=5 #m[i]=m[i]//5 l=[5,8,5,]
            if M[i]%3 == 0: 
                M[i]//=3
L = [25,8,75,12]
ChangeVal(L,4)
for i in L:
    print(i,end="#")

