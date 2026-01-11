num = int(input("Enter a number: "))
if num>0:
    print("Positive number")
elif num==0:
    print("Zero")
else:
    print("Negative number")

no = int(input("Enter a number: "))
if no%2==0:
    print("Even number")
else:
    print("odd number")

age = int(input("Enter your age: "))
if age>=18:
    print("Eligible to vote")
else:
    print("Not Eligible for vote")

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
if num1>num2:
    print(f"{num1} is greater")
elif num1 == num2 :
    print("Equal numbers")
else:
    print(f"{num2} is greater")

marks = int(input("Enter your marks: "))
if marks >= 90:
    print("A")
elif marks>=75:
    print("B")
elif marks>=50:
    print("C")
else:
    print("Fail")

a = int(input("NUMBER 1: "))
b = int(input("NUMBER 2: "))
print(["add","sub","mul","div"])
opp = str(input("enter the operation to perform: "))
if opp == "add" :
    print(a+b)
elif opp == "sub":
    print(a-b)
elif opp=="mul":
    print(a*b)
elif opp=="div":
    print(a/b)
else:
    print("Enter valid operation")
