# Hashing and maping 
# Problem Frequency of Elements 
"""____________________________Method No - 1_________________________________"""
num = [1,2,3,4,2,4,3,2,4,5,7,8,9,7,7,9]

frequency_maps= {}

for i in range(1,len(num)):
    if num[i] in frequency_maps:
        frequency_maps [num[i]] += 1
    else:
        frequency_maps [num[i]] = 1

print(frequency_maps)

"""____________________________Method No - 1_________________________________"""
num = [1,2,3,4,2,4,3,2,3,4,9,7,7,9]

hash_map = {}
n = len(num)
for i in range(0,n):
    hash_map [num[i]] = hash_map.get(num[i],0) + 1

print(hash_map)



