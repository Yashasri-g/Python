import random
print("Welcome to guessing game\nGuess a number between 1 to 100")
number = random.randint(1,100)
for i in range(1,11):
    user = int(input(f"Attempt {i}/10 - guess What do think the number is: "))
    if user == number:
        print("Woowwww!!! You guessed it right, awesome")
        break
    elif user > number:
        print("Too high! Try again")
    else:
        print("Too low!")
        print("Try again")
else:
        print("Out of attempts\t better luck next time")
print("Thanks for playing!!\nGAME OVER")
