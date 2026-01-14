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
    
# Solution 3
print("\n_______________Solution 3________________________")

n2 = [5,3,2,2,1,5,5,7,5,10]
m2 = [10,111,1,9,5,67,2]

hash_dic = {}

for num in n2:
    hash_dic[num] = hash_dic.get(num,0)+1

for num in m2:
    print(hash_dic.get(num,0))

print("\n_______________Solution 4________________________")
s = "azyxyyzaaaa"
q = ["d","a","y","x"]
hash_list1 = [0] * 26

for ch in s:
    ascii_val = ord(ch)
    index = ascii_val-97
    hash_list1[index] += 1

for ch in q:
    ascii_val = ord(ch)
    index = ascii_val-97
    print(hash_list1[index])




