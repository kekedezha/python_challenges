#number guessing game
import random

def random_number_game(name):
    player_choice = input(f"\n{name}, guess what number I am thinking of...1, 2 or 3.")

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

    random_number_game(args.name);