import random
import time
from collections import Counter

def get_computer_choice(difficulty, player_history):
    choices = ['Snake', 'Water', 'Gun']
    if difficulty == 'Hard' and player_history:
        # Counter strategy: Use the most frequently used player move to counter it
        most_common_move = Counter(player_history).most_common(1)[0][0]
        if most_common_move == 'Snake':
            return 'Gun'
        elif most_common_move == 'Water':
            return 'Snake'
        else:
            return 'Water'
    return random.choice(choices)

def determine_winner(player_choice, computer_choice):
    if player_choice == computer_choice:
        return 'Draw'
    elif (
        (player_choice == 'Snake' and computer_choice == 'Water') or
        (player_choice == 'Water' and computer_choice == 'Gun') or
        (player_choice == 'Gun' and computer_choice == 'Snake')
    ):
        return 'Player'
    else:
        return 'Computer'

def display_scoreboard(player_score, computer_score, rounds_played):
    print("\n--- Scoreboard ---")
    print(f"Rounds Played: {rounds_played}")
    print(f"Player Score: {player_score}")
    print(f"Computer Score: {computer_score}")
    print("-------------------\n")

def get_hint():
    return "Hint: Think strategically!"

def analyze_player_behavior(player_history):
    print("\n--- Player Move Analysis ---")
    move_counts = Counter(player_history)
    for move, count in move_counts.items():
        print(f"{move}: {count} times")
    print("---------------------------\n")

def snake_water_gun_game():
    print("Welcome to the Enhanced Snake-Water-Gun Game!")
    print("Rules: Snake beats Water, Water beats Gun, Gun beats Snake.")
    print("Choose your difficulty level: [Easy, Medium, Hard]")
    difficulty = input("Enter difficulty: ").capitalize()
    
    if difficulty not in ['Easy', 'Medium', 'Hard']:
        print("Invalid difficulty. Defaulting to Medium.")
        difficulty = 'Medium'

    print("How many rounds would you like to play?")
    rounds = input("Enter number of rounds: ")
    try:
        rounds = int(rounds)
    except ValueError:
        print("Invalid input. Defaulting to 5 rounds.")
        rounds = 5

    player_score = 0
    computer_score = 0
    player_history = []
    special_rounds = random.sample(range(1, rounds + 1), min(2, rounds))  # Two special rounds if possible

    for round_num in range(1, rounds + 1):
        print(f"\nRound {round_num}:")
        if round_num in special_rounds:
            print("Special Round! Points are doubled!")

        print("Choose your move: [Snake, Water, Gun]")
        start_time = time.time()
        player_choice = input("Your choice: ").capitalize()
        time_taken = time.time() - start_time

        if time_taken > 10:
            print("Too slow! You lose this round.")
            computer_score += 2
            continue

        if player_choice not in ['Snake', 'Water', 'Gun']:
            print("Invalid choice! Please choose Snake, Water, or Gun.")
            continue

        player_history.append(player_choice)
        computer_choice = get_computer_choice(difficulty, player_history)
        print(f"Computer chose: {computer_choice}")

        print(get_hint())

        winner = determine_winner(player_choice, computer_choice)

        if winner == 'Player':
            points = 4 if round_num in special_rounds else 2  # Double points for special rounds
            print(f"You win this round! You earn {points} points.")
            player_score += points
        elif winner == 'Computer':
            points = 4 if round_num in special_rounds else 2  # Double points for special rounds
            print(f"Computer wins this round! It earns {points} points.")
            computer_score += points
        else:
            print("This round is a draw! Both earn 1 point.")
            player_score += 1
            computer_score += 1

        display_scoreboard(player_score, computer_score, round_num)

    analyze_player_behavior(player_history)

    print("\nGame Over!")
    print(f"Final Scores -> Player: {player_score}, Computer: {computer_score}")

    if player_score > computer_score:
        print("Congratulations! You won the game!")
    elif player_score < computer_score:
        print("Computer wins the game! Better luck next time.")
    else:
        print("The game is a draw!")

if __name__ == "__main__":
    snake_water_gun_game()
