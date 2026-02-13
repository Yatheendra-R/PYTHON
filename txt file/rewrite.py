def rewrite():
    with open("sample_copy.txt","r")as f,open("rewrite.txt","w") as f1:
        line=f.read().split
        x1=str(line)
        print(x1)
        x="".join(x1)
        
        f1.write(x)
rewrite()
