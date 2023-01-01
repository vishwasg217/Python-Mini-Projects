import random
from traceback import print_list  
options = ['rock', 'paper', 'scissors']

compwin = 0
userwin = 0

while True:
    ip = input("Type rock/paper/scissors or Q to quit: ").lower()
    if ip == 'q':
    
        break
    if ip not in options:
        print("Please enter a valid option.")
        continue
    
    ran = random.randint(0,2)
    comp = options[ran]
    print("Computer Picked ", comp)

    if ip == 'rock' and comp == 'scissors':
        print("You win!!")
        userwin += 1

    elif ip == 'scissors' and comp == 'paper':
        print("You win!!")
        userwin += 1
    
    elif ip == 'paper' and comp == 'rock':
        print("You win!!")
        userwin += 1

    elif ip == comp:
        print("It's a tie")

    else:
        print("Computer wins")
        compwin += 1
    

print("You won ", userwin, "times.")
print("Computer won", compwin, "times.")
print("Goodbye!!")

    
