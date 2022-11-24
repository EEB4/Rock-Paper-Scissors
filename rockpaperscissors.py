import random

print ("Rock, Paper, Scissors - Shoot!")

userChoice = input("Choose your weapon [R]ock, [P]aper, or [S]cissors")

print ("Please choose a letter:")

print ("[R]ock, [P]aper, [S]cissors")

print ("You chose: " + userChoice)

choices = ['R', 'P', 'S']

opponentChoice = random.choice (choices)

print ("I chose: " + opponentChoice)

if opponentChoice == str.upper(userChoice):

    print ("Tie! ")

elif opponentChoice == 'R' and userChoice.upper() == 'S':
    print ("Scissors beats rock, I win! ")

elif opponentChoice == 'S' and userChoice.upper() == 'P':
    print ("Scissors beats paper! I win")

elif opponentChoice == 'P' and userChoice.upper() == 'R':
    print ("Paper beats rock, I win!")

else:
    print("You Win.")
