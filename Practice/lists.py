'''
Create a list of first 10 natural numbers.
Print:
First 3 elements
Last 3 elements
Alternate elements
Reversed list
'''
l = [1,2,3,4,5,6,7,8,9,10]
print(l[0:3])
print(l[-3:])
print(l[::2])
print(l[::-1])

nums = [5, 10, 15, 20, 25, 30]
print(nums[1:5])
print(nums[1::2])
print(nums[-6:])

l1=[]
l1.append(10)
l1.append(20)
l1.append(30)
l1.insert(1,15)
print(l1)

a = [1, 2]
b = [3, 4, 5]
a1 = a + b
print(a1)
a.extend(b)
print(a) 

colors = ["red", "blue", "green", "blue"]
colors.remove("blue")
colors.pop()
print(colors)

nums = [4, 2, 9, 1, 5, 2]
nums.sort()
nums.reverse()
nums.count(2)

numbers = [10, 20, 30, 40]
if 50 in numbers:
    print("Found")
else:
    print("Not Found")

nums = [12, 45, 7, 89, 23]
print(sum(nums))
print(max(nums))
print(min(nums))

nums = [12, 45, 7, 89, 23]
print((sum(nums)/(len(nums))))

# Remove all even numbers from the list:
nums = [1, 2, 3, 4, 5, 6, 7, 8]
odd = []
for i in range(len(nums)):
    if nums[i] % 2 != 0:
        odd.append(nums[i])
print(odd)

# Write a program to find the second largest number in a list.
nums = [12, 45, 7, 89, 23]
nums.sort()
print(nums[-2])

# Reverse a list without using reverse() or slicing.
nums = [12, 45, 7, 89, 23]
reve = []
i = len(nums) - 1
while i >= 0:
    a = nums[i]
    reve.append(a)
    i = i-1 
print(reve)

# Count how many positive numbers exist in a list. 
nums = [ 2, 4, 5, -1 , -6 , -7 ]
count = 0 
for i in range(len(nums)):
    if nums[i] > 0 :
        count+=1
print(count)
