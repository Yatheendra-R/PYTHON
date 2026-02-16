s1=input("Enter the word: ")
s2=input("Enter the word: ")
d1={}
d2={}
for i in s1:
    cnt=0
    if (i not in d1):
        for j in s1:
            if (i==j):
                cnt+=1
        d1[i]=cnt
#print(d1)
for i in s2:
    cnt=0
    if (i not in d2):
        for j in s2:
            if (i==j):
                cnt+=1
        d2[i]=cnt
#print(d2)
fg=1
try:
    for i in d1:
        if d1[i]!=d2[i]:
            fg=0
            break
    for i in d2:
        if d1[i]!=d2[i]:
            fg=0
            break
except Exception as e:
    #print(e)
    fg=0
if(fg):
    print("anagrams")
else:
    print("NO")
    
