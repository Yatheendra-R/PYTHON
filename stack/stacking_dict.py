def create_dict():
    mydict={}
    x=int(input("Enter the number of people: "))
    for i in range(x):
        ph=int(input("Enter the phone: "))
        name=input("Enter the name: ")
        mydict[ph]=name
    return mydict
def PUSH(mydict):
    stack=[]
    for j in mydict:
        fd=int(str(j)[0])  #converting int to str,using indexing taking
                           #the first digit and agin converting the first
                           #digit int int
        if fd%2!=0:
            stack.append(j)
    return stack
mydict=create_dict()
stack=PUSH(mydict)
if len(stack)==0:
    print("NO number starting with odd digit")
else:
    print("number starting with odd digit are")
    print(stack)
