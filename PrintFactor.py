
n = int(input('Enter any Postive Number : '))
result = []
for i in range(1,n+1):
    if (n % i == 0):
        result.append(i)
print(result)

# Time Complexity Tc = O(n)
# Space Complexity is Sc = O(k), k means which elements store in list 
"""_______________________Optimal Solution 1________________________"""
n = int(input('Enter any Postive Number : '))
result = []
for i in range(1,(n // 2)+1):
    if (n % i == 0):
        result.append(i)
result.append(n)
print(result) 
"""_______________________Optimal Solution 2________________________"""
from math import sqrt 
n = int(input('Enter any Postive Number : '))
result = []
for i in range(1,int(sqrt(n))+1):
    if (n % i == 0):
        result.append(i)
        result.append(n // i)
    
print(sorted(set(result))) 

