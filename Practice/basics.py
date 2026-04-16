# Practice: Python basics exercises
#Identify the data type of each
a = 10
b = 3.5
c = "Python"
d = True
e = None
print(type(a))
print(type(b))
print(type(c))
print(type(d))
print(type(e))
OUTPUT : 
<class 'int'>
<class 'float'>
<class 'str'>
<class 'bool'>
<class 'NoneType'>

# Write a program to store your name, age, CGPA and print them in one line.
name = "Yashasri"
age = 18
CGPA = 9
print(name,age,CGPA)
OUTPUT : 
Yashasri 18 9

# Convert the following:
''' 
"25" → integer
7 → string
"3.14" → float
'''
print(int("25"))
print(str(9))
print(float("3.14"))
OUTPUT : 
25
7
3.14

#Take two numbers as input from the user and print their sum.
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
print(f"sum of {num1} and {num2} is {num1 + num2}")
OUTPUT:
Enter first number: 5
Enter second number: 5
sum of 5 and 5 is 10

x = 10
y = 3

print(x + y)
print(x // y)
print(x ** y)
OUTPUT : 
13
3
1000

a = 5
a += 3
a *= 2
print(a)
OUTPUT : 16

print(10 > 5 and 5 < 3) # False
print(not (10 == 10)) # False

result = 10 + 2 * 5 - 3
print(result) # 17

print((5 + 3) * 2 ** 2) # 32

text = "PythonProgramming"
print(text[6:17])
OUTPUT : 
Programming

# Reverse the string "developer" using slicing.
str = "developer"
print(str[::-1]) 
OUTPUT :
repoleved

# Count the number of times 'a' appears in "data analysis"
str = "data analysis"
print(str.count("a"))
OUTPUT:
4

# Replace "Java" with "Python" in the string: "I love Java programming"
str = "I love Java programming"
print(str.replace("Java","Python"))
OUTPUT:
I love Python programming

# Write a program using f-string to print:
# My name is ___ and I am ___ years old.
name = "Yashasri"
age = 20
print(f"My name is {name} and I am {age} years old.")
OUTPUT : 
My name is Yashasri and I am 20 years old.

print("Hello\nWorld")
print("Python\tProgramming")
OUTPUT:
Hello
World
Python	Programming

# Check if "AI" is present in "Artificial Intelligence".
print("AI" in "Artificial Intelligence") # False 

text = "banana"
print(text.count("na"))
print(text.startswith("ba"))
print(text.endswith("a"))
OUTPUT : 
2
True
True

"""
Write a program that:
Takes a name from the user
Converts it to uppercase
Prints the length of the name
"""
name = input("Enter your name: ")
n = name.upper()
print(len(n))
