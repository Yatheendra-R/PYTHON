def copy():
    f=open("sample_copy.txt","r")
    f1=open("copyed.txt","w")
    line=f.readlines()
    for i in line:
        f1.write(i)
copy()
