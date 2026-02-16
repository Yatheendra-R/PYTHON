#l=[2,1,5,3,1,0,4]
#l=[3,0,1,0,4,0,2]
#l=[0,1,2,3,4,1,2,1,3,3]
#l=[3,0,2,0,4]
#l=[3,0,1,0,4,0,2]
l=[2,1,5,3,1,0,4]
dep=0
max_num=max(l)
for i in range(1,len(l)-1):
    dep+=(max_num)-l[i]
print(dep)
ind=0
new_max=max(l)
old_max=l[0]
old_max_ind=0
new_max_ind=l.index(max(l))
while True:
    if  new_max_ind==(len(l)-1):
        break
    if                                                                                                                      
    else:
        
    
"""
while True:
    
       ind1= l.index(max(l))
       dep1=abs(ind1-(ind+1))*abs(l[ind1]-l[ind])
       print("1:",dep1)
       dep-=dep1
       print(dep)
       l=l[ind1:]
       print(l)
       
       ind=ind1
print(dep)

tall=l[0]
old_tall=l[0]
old_tall_ind=0
tall_ind=0
print(dep)
for i in range(len(l)-1):
    if l[i]<l[i+1]:
        old_tall=tall
        old_tall_ind=tall_ind
        tall=l[i+1]
        tall_ind=i+1
        dep=dep-(abs(tall_ind-old_tall_ind)*abs(old_tall-tall))
        
print(dep)   
                  
dep=0
tall=l[0]
old_tall=l[0]
old_tall_ind=0
tall_ind=0
for i in range(len(l)-1):
    if l[i]>l[i+1]:
        
        dep+=tall-l[i+1]
        print(dep)
    elif l[i]<l[i+1]:
        old_tall=tall
        old_tall_ind=tall_ind
        tall=l[i+1]
        tall_ind=i+1
        if (old_tall>tall):
            dep=dep-((tall_ind-old_tall_ind)*(old_tall-tall))
            
print(dep)"""
