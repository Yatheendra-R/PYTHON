#methods in sets
#set = collection which unordered, unindexed. no duplicate values

utensils={"forks","spoon","knife"}
dishes ={"bowl","cup","plate"}
####################
utensils.add("napkin")
print(utensils)

utensils.remove("forks")
print(utensils)
#####################
utensils.update(dishes)

print("utensils")
print(utensils)

print("dishes")
print(dishes)
###################
utensils.clear()    #empty set
print(utensils)
####################
utensils={"forks","spoon","knife"}
dishes ={"bowl","cup","plate"}
x=utensils.union(dishes)   #combaining both set
print(x)
#####################

utensils={"forks","spoon","knife"}
dishes ={"bowl","cup","plate","knife"}

print(utensils.difference(dishes))   #unique in utensils 
print(dishes.difference(utensils))   #unique in dishes
print(utensils.intersection(dishes)) #common from both the set



