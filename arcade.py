from guess_number import random_number_game
from rps import rps
import sys

def arcade(name="Player_one"):
    print(f"\n{name}, welcome to the arcade!🕹️\n")

    while True:
        player_choice = input(f"Please choose a game to play: \n1 = Rock, Paper, Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the arcade.\n\n")
        if player_choice.lower() not in ["1","2","x"]:
            continue
        else:
            break

    if player_choice == "2":
        random_number_game(name)
    elif player_choice == "1":
        rps(name)
    else:
        sys.exit(f"\n\nSee you next time!\nBye {name}!✌🏽")

#only run file if in 
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

    arcade(args.name)
    