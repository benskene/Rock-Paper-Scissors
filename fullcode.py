import random
#Ask the user to choose rock, paper, or scissors
def get_user_choice():
    choice = input("Choose rock, paper, or scissors: ").lower()
    while choice not in ["rock", "paper", "scissors"]:
        choice = input("Invalid choice. Please choose rock, paper, or scissors: ").lower()
    return choice

#Pick a random choice for the computer
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

#Determine the winner based on the choices
def determine_winner(user, computer):
    if user == computer:
        return "tie"
    elif (
        (user == "rock" and computer == "scissors") or
        (user == "paper" and computer == "rock") or
        (user == "scissors" and computer == "paper")
    ):
        return "user"
    else:
        return "computer"

# Main game loop
def play_game():
    user_score = 0
    computer_score = 0

    while user_score < 2 and computer_score < 2:
        print(f"\nScore — You: {user_score} | Computer: {computer_score}")
        user = get_user_choice()
        computer = get_computer_choice()
        print(f"The computer chose {computer}.")

        result = determine_winner(user, computer)
        if result == "user":
            print("You win this round!")
            user_score += 1
        elif result == "computer":
            print("Computer wins this round")
            computer_score += 1
        else:
            print("It's a tie!")
            
#Final score after 2 wins
    print("\n=== Final Score ===")
    print(f"You: {user_score} | Computer: {computer_score}")
    if user_score > computer_score:
        print("You win!")
    else:
        print(" Computer wins!")

#Loop to play the game multiple times
while True:
    play_game()
    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing!")
        break
