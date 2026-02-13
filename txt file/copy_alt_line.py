def copyaltline():
    with open("sample_copy.txt","r")as f,open("altlinecopy.txt","w")as f1:
        line=f.readlines()
        a=2
        for i in line:
            if a%2==0:
                f1.write(i)
            a+=1
copyaltline()
