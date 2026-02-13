def notacopy():
    f=open("sample_copy.txt","r")
    f1=open("notacopyed.txt","w")
    line=f.readlines()
    for i in line:
        if "a" not in i:
            f1.write(i)
notacopy()
