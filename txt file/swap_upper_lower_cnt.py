
with open("swape_upper_lower.txt","r") as f1:
    with open("temp.txt","w") as f2:
        listr=f1.readlines()
        cnt=0
        for i in listr:
            L=i.split()
            STRadd=""
            for j in L:
                Str=""
                for k in j:
                    if k.isupper():
                        Str+=k.lower()
                        cnt+=1
                    else:
                        Str+=k
                STRadd+=Str
                STRadd+=" "
            f2.write(STRadd)
            f2.write("\n")
print("number of upper case swaped is: ",cnt)
            
                    
                    
                    
