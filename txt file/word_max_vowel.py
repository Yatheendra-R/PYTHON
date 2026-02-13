
def wordmaxvowel():
    with open("word_maxvowel.txt","r") as f:
        
        x=f.read().split()
        l=[]
        for k in x:
            c=0
            for j in k:
                if j in "AEIOUaeiou":
                    c+=1
            l.append(c)
        m=max(l)
        ind=l.index(m)
        
        print(x[ind])
wordmaxvowel()
