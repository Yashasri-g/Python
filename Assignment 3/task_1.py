n = int(input("Enter a number: "))
def factorial(n):
	if n==0 or n==1:
		return 1
	else:
		res = n * factorial(n-1)
		return res
print(f"Factorial of {n} is : {factorial(n)}")
