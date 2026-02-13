def swap():
        with open("swape_upper_lower.txt","r") as f1:
                cnt=0
                Str=f1.read()
                for i in Str:
                    if i.isupper():
                        cnt+=1
                print("Number upper case swaped: ",cnt)
        with open("swape_upper_lower.txt","r") as f1:
                with open("temp1.txt","w") as f2:
                    l=f1.readlines()
                    for j in l:
                        f2.write(j.lower())
swap()
