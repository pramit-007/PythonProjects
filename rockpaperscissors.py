import random

computer = random.choice([-1, 0, 1])

youstr = input("Enter your choice (r for Rock, p for Paper, s for Scissors): ")

youDict = {"r": 1, "p": -1, "s": 0}
reverseDict = {1: "Rock", -1: "Paper", 0: "Scissors"}

if youstr in youDict:
    you = youDict[youstr]

    print(f"You chose {reverseDict[you]}\nComputer chose {reverseDict[computer]}")

    if (computer == you):
        print("Game Draw")
    else:
        if (computer == -1 and you == 1):
            print("You lose!")
        elif (computer == -1 and you == 0):
            print("You win!")
        elif (computer == 1 and you == -1):
            print("You win!")
        elif (computer == 1 and you == 0):
            print("You lose!")
        elif (computer == 0 and you == 1):
            print("You win!")
        elif (computer == 0 and you == -1):
            print("You lose!")
        else:
            print("Something went wrong!")  
else:
    print("Invalid choice. Please enter 'r', 'p', or 's'.")
