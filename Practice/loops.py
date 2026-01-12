for i in range(1,21):
    print(i)

n = int(input("enter a number: "))
print(f"Sum from 1 to {n} is {n*(n+1)/2}")

st = "Internship"
vowels = ['a','e','i','o','u','A','E','I','O','U']
count=0
for i in st:
    if i in vowels:
        count+=1
print(count)

for i in range(1,51):
    if i%2!=0:
        continue 
    else:
        print(i)

  n = int(input("enter a number:"))
for i in range(1,11):
    print(f"{n} x {i} = {n*i}")

lst = [4,7,3,2,5]
largest = lst[0]
for i in lst:
    if largest<i:
        largest=i
print(f"The largest number is {largest}")

lst = [4,7,3,2,5]
small = lst[0]
for i in lst:
    if small>i:
        small=i
print(f"The smallest number is {small}")

lst = [4,-7,3,2,-5,0,0]
z = p = n = 0
for i in lst:
    if i == 0 :
        z+=1
    elif i < 0 :
        n+=1
    else:
        p+=1
print(f"positive: {p}, negative:{n}, zeros:{z}")

while True:
    password=str(input("enter the password: "))
    if password=="python123":
        print("logged in")
        break
    else:
        print("try again")

  n = int(input("enter a number: "))
no = str(n)
total = 0 
for i in no:
    total+=int(i)
print(f"Sum of digits in the given number {n} is {total}")

n = int(input("Enter a number: "))

if n <= 1:
    print(f"{n} is not a prime number")
else:
    is_prime = True
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

    if is_prime:
        print(f"{n} is a prime number")
    else:
        print(f"{n} is not a prime number")
