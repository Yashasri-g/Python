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
print(str(7))
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
