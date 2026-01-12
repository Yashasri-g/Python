import random
print("Welcome to the game of rolling dice 🎲")
while True:
    choice = input("Enter 'roll' to play or 'q' to quit: ").lower()
    if choice == "q":
        print("Thanks for playing 😊")
        break
    elif choice == "roll":
        print("Rolling the dice...")
        print("You got:", random.randint(1, 6))
    else:
        print("Enter a valid input")
