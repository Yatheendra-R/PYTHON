a=[6,4,7,3]
x=len(a)
y=max(a)
z=min(a)
b=[x,y,z]
print(b)

for i in range(min(a),max(a)):
      print()
      for j in range(i,0,-1):
          print(j,end="")
      
