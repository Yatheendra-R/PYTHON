x=44
def varscope(var):
    x=22
    print("varscope's x=",x)
    x=89
    print("varscope's x=",x)

def accessGval():
    global x
    x=77
    print("Before x=",x)
    x=56
    print("x=",x)
    varscope(x)
    print("After x =",x)
#main
x=89
print("at main before=",x)
x=98
print("at main=",x)
accessGval()
x=100
print("at main after=",x)
