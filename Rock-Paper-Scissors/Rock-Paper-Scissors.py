import random

CHOICES = ['rock', 'paper', 'scissors']
WIN_CONDITIONS = {
    'rock': 'scissors',
    'scissors': 'paper',
    'paper': 'rock'
}

def get_user_choice() -> str:
    while True:
        user_input = input("\nYour turn! Choose [rock/paper/scissors]: ").strip().lower()
        if user_input in CHOICES:
            return user_input
        # Auto-correct common abbreviations
        if user_input.startswith('r'): return 'rock'
        if user_input.startswith('p'): return 'paper'
        if user_input.startswith('s'): return 'scissors'
        print("Invalid choice. Please enter rock, paper, or scissors.")

def determine_winner(user: str, computer: str) -> str:
    if user == computer:
        return 'tie'
    return 'user' if WIN_CONDITIONS[user] == computer else 'computer'

def print_result(user: str, computer: str, result: str) -> None:
    print(f"\nYou chose: {user.capitalize()}")
    print(f"Computer chose: {computer.capitalize()}")
    print("\n" + "═" * 30)
    if result == 'tie':
        print("It's a tie!")
    else:
        winner = "You win! " if result == 'user' else "Computer wins! "
        print(f"{winner} {user.capitalize()} beats {computer.capitalize()}!")

def play_round() -> tuple:
    user_choice = get_user_choice()
    computer_choice = random.choice(CHOICES)
    result = determine_winner(user_choice, computer_choice)
    print_result(user_choice, computer_choice, result)
    return result

def main():
    print("══════════════════════════════")
    print(" Rock-Paper-Scissors Game ")
    print("══════════════════════════════")
    print("Game Rules:")
    print("- Rock beats Scissors")
    print("- Scissors beats Paper")
    print("- Paper beats Rock\n")

    user_score = 0
    computer_score = 0
    rounds = 0

    while True:
        rounds += 1
        print(f"\nRound {rounds}")
        result = play_round()

        if result == 'user':
            user_score += 1
        elif result == 'computer':
            computer_score += 1

        print("\nScoreboard:")
        print(f"You: {user_score}  |  Computer: {computer_score}")

        while True:
            replay = input("\nPlay again? [y/n]: ").lower()
            if replay in ['y', 'n']:
                break
            print("Please enter 'y' or 'n'")
        
        if replay == 'n':
            print("\n══════════════════════════════")
            print(f"Final Score after {rounds} rounds:")
            print(f"You: {user_score}  |  Computer: {computer_score}")
            print("Thanks for playing!")
            break

if __name__ == "__main__":
    main()