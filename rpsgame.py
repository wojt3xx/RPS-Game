import random
import sys


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''


user_points = 0
computer_points = 0

def print_result():
    print(f'You have {user_points} points and computer has {computer_points} points.')


def the_game():
    
    user_choice = input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n")
    computer_choice = random.randint(0, 2)

    user_choice = int(user_choice)
    
    global user_points
    global computer_points
    
    if user_choice == 0 and computer_choice == 0:
        print(rock)
        print("Computer choice:")
        print(rock)
        print("Draw!")
        print_result()
    elif user_choice == 0 and computer_choice == 1:
        print(rock)
        print("Computer choice:")
        print(paper)
        print("You Lose!")
        user_points -= 1
        computer_points += 1
        print_result()
    elif user_choice == 0 and computer_choice == 2:
        print(rock)
        print("Computer choice:")
        print(scissors)
        print("You Won!")
        user_points += 1        
        computer_points -= 1
        print_result()
    elif user_choice == 1 and computer_choice == 0:
        print(paper)
        print("Computer choice:")
        print(rock)
        print("You Won!")
        user_points += 1
        computer_points -= 1
        print_result()
    elif user_choice == 1 and computer_choice == 1:
        print(paper)
        print("Computer choice:")
        print(paper)
        print("Draw!")
        print_result()
    elif user_choice == 1 and computer_choice == 2:
        print(paper)
        print("Computer choice:")
        print(scissors)
        print("You Lose!")
        user_points -= 1
        computer_points += 1
        print_result()
    elif user_choice == 2 and computer_choice == 0:
        print(scissors)
        print("Computer choice:")
        print(rock)
        print("You Lose!")
        user_points -= 1
        computer_points += 1
        print_result()
    elif user_choice == 2 and computer_choice == 1:
        print(scissors)
        print("Computer choice:")
        print(paper)
        print("You Won!!")
        user_points += 1
        computer_points -= 1
        print_result()
    elif user_choice == 2 and computer_choice == 2:
        print(scissors)
        print("Computer choice:")
        print(scissors)
        print("Draw!")
        print_result()

    play_again = input("Do you want to play again? (yes|no)\n")

    if play_again == "yes":
        the_game()
    elif play_again == "no":
        print(f"Game finished. You got {user_points} points and computer got {computer_points} points in this game.")
        exit
    else:
        print("Wrong answer!")
        exit


the_game()