t = (1,2,3,4,5)
print(t[0])
print(t[-1])
print(t[1:len(t)-1])

t = (10, 20, 30, 40, 50)
print(t[1:4])
print(t[0::2])
print(t[::-1])

t = (5, 10, 15, 20, 25)
if 25 in t:
    print("Found")
else:
    print("Not Found")

t1 = (1, 2)
t2 = (3, 4, 5)
print(t1+t2)

t = (1, 3, 5, 3, 7, 3)
print(t.count(3))

lst = [10, 20, 30]
t = (10, 20, 30)
lst[0]=100
t = list(t)
t[0]=100
t = tuple(t)
print(t)
print(type(t))
print(lst)
print(type(lst))

nums = [1, 2, 2, 3, 4, 4, 5]
nums = set(nums)
print(nums)
print(type(nums))

s = {10, 20, 30, 40}
s.add(50)
s.discard(20)
print(s)

s = {5, 10, 15, 20, 25}
print(30 in s)

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
print(A|B)
print(A&B)
print(A-B)

set1 = {10, 20, 30}
set2 = {20, 30, 40}
print(f"Common elements: {set1&set2}")

s = {1, 2, 3, 4}
f = frozenset(s)
print(f)
# cant add as its immutable 

d = {"Name":"Shilpa","Age":34,"City":"Hyderabad"}
print(d,type(d))

student = {
    "name": "Ravi",
    "marks": 85,
    "grade": "A"
}
student["marks"]=90
student["city"]="Mumbai"
print(student)

student = {
    "name": "Anu",
    "marks": 78,
    "grade": "B"
}
student.pop("grade")
print(student)

employee = {
    "id": 101,
    "name": "Kiran",
    "salary": 45000
}
print(employee.keys())
print(employee.values())

nums = [2, 4, 6, 8, 10]
for num in nums:
    print(num)

text = "Python"
for i in text:
    print(i)

my_dict = {'apple': 3, 'banana': 6, 'orange': 4}

for key, value in my_dict.items():
    print(f"The key is: {key}, and the value is: {value}")

my_dict = {'apple': 3, 'banana': 6, 'orange': 4}

for value in my_dict.values():
    print(f"the value is: {value}")

s = {1,2,3,4,6,7,8,90,54,656,432}
count=0
for i in range(len(s)):
    count+=1
print(count)

marks = {
    "Maths": 80,
    "Science": 75,
    "English": 85
}
print(sum(marks.values()))

my_dict = {'apple': 50, 'banana': 120, 'cherry': 80, 'date': 20}
print(max(my_dict,key=my_dict.get))

t = (1, 2, 3, 4, 5, 6)
count=0
for i in range(len(t)):
    if t[i]%2==0:
        count+=1
print(count)

my_list = [1, 2, 3, 4, 1, 2, 5]
t = tuple(my_list)
s = set(my_list)
print(t,type(t))
print(s,type(s))
