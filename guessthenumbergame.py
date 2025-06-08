import random

n= random.randint(1,100)

a=-1
guesses=0

while(a!=n):
    guesses+=1
    a = int(input("Enter the number:"))
    if(a>n):
        print("Lower number please!")
    elif(a<n):
        print("Higer number please!")
    else:
        break            



print(f"You have guessed correctly the number {n} in {guesses} attempts")
