# Find missing number (1 to n)
n = 9
s = [1,3,4,2,7,8,9,6]
n_sum = sum(range(1,n+1))
a_sum = 0 
for i in s:
    a_sum+=i
miss = n_sum-a_sum
print(f"The missing number is {miss}")

# Find intersection of two arrays
# Find union of two arrays
a = [1,2,3,4,5,6,0]
b = [56,6,78,9,3]
a = set(a)
b = set(b)
print(f"Intersection:{a&b}")
print(f"Union: {a|b}")
