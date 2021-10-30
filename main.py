import random


def game(user, computer):

    rock = 0
    paper = 1
    scissors = 2

    if user != computer:
        if  user == 0 and computer == 1:
            print("Paper covers rock, computer wins!")
        elif user == 1 and computer == 0:
            print("Paper covers Rock,You win!")
        elif user == 0 and computer == 2:
            print("Rock Smashes scissors, You win!")
        elif user == 2 and computer == 0:
            print("Rock Smashes scissors, Computer wins!")
        elif user == 1 and computer == 2:
            print("Scissors cuts paper, Computer Wins!")
        elif user == 2 and computer == 1:
            print("Scissors cuts paper,You win!")
        else:
            print("It's tie")
    else:
        print("It's tie")


print("Welcome to Rock ,Paper and Scissors Game!")


user_input = int(input("Enter 0 as rock, 1 as paper or 2 as scissors:\n"))
print(f"You chose {user_input}")

computer_input= random.randint(0,2)
print(f"And computer chose {computer_input}")

game(user_input,computer_input)