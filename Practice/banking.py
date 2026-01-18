# A simple banking application
# check balance
# withdraw 
# deposit 
def check_balance():
    global b 
    print(f"The current balance is {b}")
def withdraw(a):
    global b 
    if b < a:
        print("Insufficient balance")
    else:
        b -= a
        print(f"Withdrawn: {a}")
        check_balance()
def deposit(d):
    global b
    b += d
    print("Deposit successful")
    check_balance()

b = 0.0

print("Welcome to paradise bank")
while True:
    print("1. Check balance")
    print("2. Withdraw amount")
    print("3. Deposit amount")
    print("4. Quit")
    c = input("Enter your choice(1-4): ")
    if c =='1':
        check_balance()
    elif c=='2':
        a = int(input("enter the amount to withdraw: "))
        withdraw(a)
    elif c=='3':
        d = int(input("enter amount to deposit: "))
        deposit(d)
    elif c=='4':
        break
    else:
        print("Invaild option")
print("Thanks for banking with us")
