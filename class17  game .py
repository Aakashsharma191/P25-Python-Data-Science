'''import random

com = random.randint(1,3)

#1 - Rock
#2 - Paper
#3 - Scissors
print("1 - Rock, 2 - Paper, 3 - Scissors")
user = int(input("Select your option :- "))

if user == com:
    print("its a drao!")
elif user == 1 and com == 3:
    print("You Won ")
elif user == 2 and com == 1:
    print("You won")
elif user == 3 and com == 2:
    print("You Won ")
else:
    print("Computer Won ")'''

#1 - Rock
#2 - Paper
#3 - Scissors

import random
com_score = 0
user_score = 0

while True:
    print()
    print()
    print()
    print()
    print()
    if user_score == 5:
        print(f"congratulation You are win : User score {user_score}  computer score {com_score} ")
        break

    elif com_score == 5:
        print(f"Congratulation computer Win : Computer score {com_score}  user score {user_score}")
        break

    print(f"Score = computer - {com_score}, User - {user_score}")
    com = random.randint(1,3)

    print("1 - Rock, 2 - Paper, 3 - Scissors")
    user = int(input("Select your option :- "))
    if user >= 1 and user <= 3:

        if user == com:
            print("its a drao!")
        elif user == 1 and com == 3:
            print("You Won ")
            user_score += 1
        elif user == 2 and com == 1:
            print("You won")
            user_score += 1
        elif user == 3 and com == 2:
            print("You Won ")
            user_score += 1
        else:
            print("Computer Won ")
            com_score += 1
    else:
        print("You are idiots 1 - 3")