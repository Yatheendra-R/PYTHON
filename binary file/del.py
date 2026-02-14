import pickle,os
'''with open("student.dat","wb") as f:
    num=int(input("Enter the number of students"))
    for i in range(num):
        x=int(input("roll number"))
        to=int(input("total"))
        pickle.dump([x,to],f)
with open("student.dat","rb") as f1:
    with open("rename.dat","wb") as f2:
        try:
            while True:
                l=pickle.load(f1)
                if l[0]==1:
                    pickle.dump(l,f2)
        except EOFError:
            pass
        
with open("rename.dat","rb") as f3:
    try:
        while True:
            l1=pickle.load(f3)
            print(l1)
    except EOFError:
        pass'''
os.remove("student.dat")
os.rename("rename.dat","students.dat")
