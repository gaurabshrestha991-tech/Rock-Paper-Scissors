import random  #tells Python to load the random module, which contains functions for generating random numbers and making random selections.

print("=== Rock, Paper, Sicssors ===")

choices = ["rock", "paper", "sicssors"]

user_choice = input("Enter rock, paper or sicssors: ").lower()

computer_choice = random.choice(choices)

print("Computer chose: ", computer_choice)

if user_choice == computer_choice:
    print("It's a tie!")

elif (user_choice == "rock" and computer_choice == "sicssors") or \
     (user_choice == "sicssors" and computer_choice == "paper") or \
     (user_choice == "paper" and computer_choice == "rock"):
     print("You Win!")

elif user_choice in choices:
    print("Computer Win!")

else:
    print("Invalid choice!.Please choose a correct choice!")



