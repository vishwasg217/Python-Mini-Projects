from operator import truediv
import random

print("Welcome to the number guessing game!")


while True:
    low = input("Enter the lower limit: ")
    if low.isdigit():
        low = int(low)
        if low < 0:
            print("Please enter a number greater than or equal to 0.")
        else:
            break
    else:
        print("Please enter only numbers:")

while True:
    upp = input("Enter the upper limit: ")
    if upp.isdigit():
        upp = int(upp)
        if upp <= 0:
            print("Please enter a number greater than 0.")
        else:
            break
    else:
        print("Please enter only numbers: ")

num = random.randint(low, upp)

g = 0

while True:
    guess = input("Guess a number: ")
    if guess.isdigit():
        guess = int(guess)
        if guess>=low and guess <=upp:
            if guess == num:
                print("You guessed it right!!")
                break
            elif guess > num:
                print("You were above the number!")
                g += 1
            else:
                print("You guessed below the number!")
                g += 1
        else:
            print("Please guess a number between", low, "and", upp)

print("You guessed it in ",g, " guesses.")
            

