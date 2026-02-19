
#generally used in looping 

sample_range=range(1,11,2)
print(sample_range)
print(type(sample_range))
for i in sample_range:
    print(i)

print(sample_range[::-1])
rev_sample_range=sample_range[::-1]
for i in rev_sample_range:
    print(i)
