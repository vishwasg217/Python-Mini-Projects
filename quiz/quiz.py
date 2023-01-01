print('\nWelcome to the football quiz game!!\n')

name = input("Please enter your user name: ")
if name.lower() == 'vishwas':
    print("Welcome back " + name + "!!")
else:
    print("Incorrect username.")
    quit()

cont = input("Do you want to play the quiz? ")
if cont.lower() != 'yes':
    print("See you soon!")
    quit()
else:
    print("Let's play!!!!")

x = 0

ans = input("Who is the Greatest Player of All Time? ")
if ans.lower() == 'lionel messi':
    print("Correct Answer!")
    x += 1
else:
    print("Incorrect answer")

ans = input("Who wears the no.16 jersey for FC Barcelona? ")
if ans.lower() == 'pedri':
    print("Correct Answer!")
    x += 1
else:
    print("Incorrect answer")

ans = input("Which player has won the most amount of titles in football?")
if ans.lower() == 'dani alves' :
    print("Correct Answer!")
    x += 1
else:
    print("Incorrect answer")

ans = input("Which is the only team to win the treble twice? ")
if ans.lower() == 'fc barcelona':
    print("Correct Answer!")
    x += 1
else:
    print("Incorrect answer")

print("That's the end!")
print("You got " + str(x) + "/4 questions correct.")
print("Percentage: " + str((x/4)*100) + "%")





