#number guessing game
import random

def random_number_game(name):
    game_count = 0
    player_wins = 0

    def play_game():
        nonlocal player_wins
        nonlocal game_count

        random_number = random.choice("123")
        player_choice = input(f"\n{name}, guess what number I am thinking of...1, 2 or 3.\n\n")

        print(f"\n{name} you chose {player_choice}.")
        print(f"I was thinking about the number {random_number}")

        
        if player_choice == random_number:
            player_wins += 1
        game_count += 1

        print(f"Game count: {game_count}")
        print(f"{name}'s wins: {player_wins}")

    return play_game

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(
        description="Provides a personal greeting for the guessing game"
    )

    parser.add_argument(
        "-n", "--name", metavar="name",
        required=True, help="The name of the person to greet."
    )

    args = parser.parse_args()

    rng = random_number_game(args.name);
    rng()