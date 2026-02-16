larr=[900,940,950,1100,1700,1800]
ldp=[1905,1200,1910,1920,1900,2000]
#larr=[1000,935,1100]
#ldp=[1200,1240,1130]
larr.sort()
ldp.sort()
min_pt=0
curr_pt=0
for i in range(len(larr)):
    check_less=0
    for j in range(len(ldp)):
        if (larr[i]>ldp[j]):
            check_less+=1
    print(check_less)
    if (i==check_less or check_less==(i-1)):
        curr_pt=1
        if curr_pt>min_pt:
            min_pt=curr_pt
    else:
        curr_pt=i
        if curr_pt>min_pt:
            min_pt=curr_pt
if (check_less==0):
    min_pt=len(larr)
print(min_pt)
    
