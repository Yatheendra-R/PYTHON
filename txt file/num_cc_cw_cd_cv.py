def num_all():
    with open("num_cc_cw_cd_cv.txt","r") as f:
        cc=cv=cd=cw=0
        x=f.read().split()
        for i in x:
            if i.isalpha():
                cw+=1
            for j in i:
                if j.lower() in "aeiou":
                    cv+=1
                if j in "1234567890":
                    cd+=1
                if j.lower() not in "aeiou" and j.lower().isalpha():
                    cc+=1
                


        return cw,cv,cc,cd
r=num_all()
print("number of words: ",r[0],"number of vowels: ",r[1],"number of consonants: ",r[2],"number of digit: ",r[3])
                
                    

        
        
                    
        
        
