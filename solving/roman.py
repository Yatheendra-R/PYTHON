value=0
s=input("Enter")
#d={"l":1,"X":10,"L":50,"C":100,"D":500,"M":1000}
L=["I","V","X","L","C","D","M"]
L1=[1,5,10,50,100,500,1000]
i=0
while True:
    if (i==len(s)):
        break
    elif (i!=len(s)-1):
        if (L.index((s[i+1]))>L.index((s[i]))):
            #print("1: ",i)
            value+=L1[(L.index((s[i+1])))]-L1[(L.index((s[i])))]
            i+=2
            #print(value)
        else:
            #print("2: ",i)
            value+=L1[(L.index((s[i])))]
            i+=1
            #print(value)
    else:
            #print("2: ",i)
            value+=L1[(L.index((s[i])))]
            i+=1
            #print(value)
print(value)
