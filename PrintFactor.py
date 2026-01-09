n = int(input('Enter any Postive Number : '))
result = []
for i in range(1,n+1):
    if (n % i == 0):
        result.append(i)
print(result)

# Time Complexity Tc = O(n)
# Space Complexity is Sc = O(k), k means which elements store in list 
