with open("sampleq_poem.txt","r") as f:
    cnt3=0
    hcnt=0
    wcnt=0
    l=f.readlines()
    for i in l:
        if i[0].lower()=="h":
            
            hcnt+=1
        elif i[0].lower()=="w":
            wcnt+=1
        print(i)
        for j in i.split():
            if len(j)==3:
                cnt3+=1
print("3",cnt3)
print("w",wcnt)
print("h",hcnt)
