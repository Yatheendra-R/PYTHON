#nesting of set
set1=set[1,2,3]
print(set1)
set2={1.2,3,"hi"}
print(set2)
set3={1,2,3,3}
print(set3)
#set4={5,6,7,set3}
#print(set4)
#set4={5,6,7,{1,2,4}}
#set4={5,6,7,[1,2,4]}
set5={5,6,7,(1,2,4)}
print(set5)
set6={5,6,7,(1,5,4)}
print(set6)


