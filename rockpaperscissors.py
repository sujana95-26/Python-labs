
import random



def play_game():
    print("Play Rock-Paper-Scissors!")
    options = ["rock", "paper", "scissors"]
    user_choice = input("Enter your choice (rock/paper/scissors): ")
    computer_choice = random.choice(options)
    print(f"You chose {user_choice}, computer chose {computer_choice}")
    if user_choice == computer_choice:
        return "Tie!"
    elif user_choice == "rock" and computer_choice =="scissors":
        return "User won"
    elif user_choice == "paper" and computer_choice == "rock":
        return "User won"  
    elif user_choice == "scissors" and computer_choice == "paper":
        return "User won" 
    else:
        return "Computer won"

num_rounds = 0  
user_wins = 0
computer_wins = 0
play_again = "y"    

while play_again == "y":
    num_rounds += 1
    result = play_game()
    if result == "user won":
        user_wins +=1
        print("user wins")
    elif result =="computer":
        computer_wins +=1
        print("computer wins")
    else:
        print("tie game")
    print("The number of rounds played: ",num_rounds)
    print("User wins: ", user_wins)
    print("Computer wins:", computer_wins)
    play_again = input("Do you want to play again? (y/n): ")
    if play_again.lower() != "y":
        break
