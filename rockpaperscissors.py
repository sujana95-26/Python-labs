import random

def play_game():
    print("Play Rock-Paper-Scissors!")
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(options)
    print(f"You chose {user_choice}, computer chose {computer_choice}")
    if user_choice == computer_choice:
        print("Tie!")
    elif user_choice == "rock" and computer_choice =="scissors":
        print("User won")

    elif user_choice == "paper" and computer_choice == "rock":
        print("User won")
    elif user_choice == "scissors" and computer_choice == "paper":
        print("User won")
    else:
        print("Computer won") 
while True:
    play_game()
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() == "y":
        continue
