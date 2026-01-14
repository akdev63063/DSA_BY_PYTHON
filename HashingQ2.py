# Solution 1
n = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]

for num in m:
    count = 0
    for i in n :
        if i == num:
            count += 1
    print(count,end = " ")

print("\n___________________________________________")

# Solution 2
print("\n")

n1 = [5,3,2,2,1,5,5,7,5,10]
m1 = [10,111,1,9,5,67,2]
hash_list = [0] * 11
for num in n1:
    hash_list[num] += 1

for num in m1:
    if num < 0 or num > 10:
        print(0)
    else:
        print(f"{num} {hash_list[num]}")
    
    
