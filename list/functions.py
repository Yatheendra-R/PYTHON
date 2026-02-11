#functions
l=[11,21,31]
print(l)
print()

#del 
del l[1]    #[index}
print(l)
print()

del l           #del full list from the address
#print(l)       #error  

l=[11,21,31]
print(l," created a new list")
print()

del l[:]
print(l)        #EMPTY LIST
print()
#pop

l1=[10,20,30]
print(l1)
print()

print(l1.pop(0))    #l1.pop(0) is index #it is printing the number which is going to get poped out
print()
print(l1)
print()

l1.pop()        #remove last element
print(l1)  
print()

l7=[]
#l7.pop()   #index error

#index

l3=[50,60,70,80]

print(l3.index(70))     #l3.index(70), 70 is the value is the list
print()

#print(l3.index(100))     #l3.index(100), 100 is the value is the list, if value is not present value error


#append (we can only add one element,only at the last of the list) 

l4=[100,200,300]

l4.append('cs')         #l4.append('cs'), cs is the value which is going to be added to the list 
print(l4)
print()

#l4.append(1,2)         #type error

#l4.append([1,2,3,3],5) #type errror

l4.append([1,2,3,3])        #adding a list
print(l4)
print()

l4[0]='yathi'               #adding with index value
print(l4)
print()

#l4[6]='ya'     #index out of range

l4[4][2]='win'      #adding in side the nested list
print(l4)
print()

#extend         (we can add more element,only at the at of the list)

l5=[10,20]

l5.extend([30,40])  #l5.extend([30,40]),([30,40]) is value which is going be added to the end of the list,to be add as list
print(l5)
print()

l5.extend([70])   
print(l5)
print()

l5.extend([[100]])      #adding nested list
print(l5)
print()

#l5.extend(60)  #error should be added as list

#len
print(l5)
print()
print(len(l5))  #lenght of the list
print()

#insert

l6=[110,112,113]
print(l6)
print()

l6.insert(1,111)    #(1,111) (index,value)
print(l6)
print()

l6.insert(3,'yathi')
print(l6)
print()

l6.insert(1000,114)     #if index not correct value added at last
print(l6)
print()

#l6.insert(114)      #type error


#remove

l7=[100,99,98,97]
print(l7)
print()

l7.remove(98)       #98 is a value in the list
print(l7)
print()

#l7.remove(1000)    #type error(1000 not found in the list)

#l7.remove()    #type error

#clear

l8=[1,2,3,4]
l8.clear()          #l8.clear()== del l8[:]
print(l8)
print()

#count

l9=[1,2,3,4,4,6,4,6,8,9]

print(l9)
print()
print(l9.count(4),' times of 4 has accoured in the list')
print()

#reverse

l10=[10,20,30,4,40,60,44,6,8,90]
print(l10)
print()

l10.reverse()  #reverse the element in the list
print(l10)
print()

l112=reversed(l10)
print(l112)
print(list(l112)) #out_put [90, 8, 6, 44, 60, 40, 4, 30, 20, 10]
print()

#sorted (default increasing order)

l11=[20,50,10,30]
print(l11)
print()

l11.sort()   #incre. order
print(l11)
print()

l11.sort(reverse=True)  #derc order
print(l11)
print()

l11_o=sorted(l11)
print(l11_o)
print()
#deep copy 
l12=[1,2,3,4,5]
l13=l12.copy()  #changing in this will not affect the orginal list
l13[0]=100
print(l12)
print(l13)
print()

#shallow copy
l14=[1,2,3,4,5]
l15=l14    #changing in this will affect the orginal list(also changes the orginal list )
l15[0]=100
print(l14)
print(l15)
print()

#upacking the list
l16=[1,2,3,4,5]
l17=[*l16]
l17[0]=100   #changing in this will not affect the orginal list
print(l16)
print(l17)
print()
