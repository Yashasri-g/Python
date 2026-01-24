# Basics

# Find the largest element in an array
s = [1,5,6,7,8,9]
maxn = s[0] 
for i in range(len(s)):
    if s[i]>max:
        maxn =s[i]
print(maxn)

# Find the smallest element
s = [1,5,6,7,8,9]
minn = s[0]
for i in range(len(s)):
    if s[i]<=minn:
        minn=s[i]
print(minn)

# Find the second largest element
s = [1,5,6,7,8,9]

max1 = float('-inf')
max2 = float('-inf')

for num in s:
    if num > max1:
        max2 = max1
        max1 = num
    elif num > max2 and num != max1:
        max2 = num

print("Second largest:", max2)

# Count even and odd numbers
s = [4,6,3,2,16,8,9,0]
count_e=0
count_o=0
for i in s :
    if i%2==0:
        count_e+=1
    else:
        count_o+=1
print(f"No.of even number in array:{count_e}")
print(f"No.of odd number in array:{count_o}")

# Count positive, negative and zeros
s = [1,6,0,-6,-8]
p = n = z = 0 
p = sum(1 for i in s if i>0)
n = sum(1 for i in s if i<0)
z = sum(1 for i in s if i==0)
print(f"positive:{p}, negative:{n}, zero:{z}")

# Reverse an array (without slicing)
s = [1,5,6,7,8,9]
res=[]
for i in range(len(s)-1,-1,-1):
    res.append(s[i])
print(res)

# Check if array is sorted (increasing)
s = [4,6,3,2,16,8,9,0]

for i in range(len(s) - 1):
    if s[i] > s[i + 1]:
        print("not sorted")
        break
else:
    print("sorted")

# Calculate sum and average
s = [1,5,6,7,8,9]
total = 0
for i in s:
    total+=i
if len(s) > 0:
    average = total / len(s)
else:
    average = 0
print(f"Sum of array:{total}")
print(f"average of array:{average}")
