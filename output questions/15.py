import random
AR=["red","green","yellow","orange","blue","black"]
P =random.randint(1,3)
Q =random.randint(2,4)
for i in range(P, Q +1):
    print (AR[i], end="-")
