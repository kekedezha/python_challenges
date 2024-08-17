from guess_number import random_number_game
from rps import rps
import sys

def arcade(name="Player_one"):
    welcome_back = False

    while True:
        if welcome_back == True:
            print(f"\n{name}, welcome back to the arcade!🕹️\n")

        player_choice = input(f"Please choose a game to play: \n1 = Rock, Paper, Scissors\n2 = Guess My Number\n\nOr press 'x' to exit the arcade.\n\n")
        if player_choice.lower() not in ["1","2","x"]:
            print(f"{name}, please enter 1, 2, or x.")
            return arcade(name)
        welcome_back = True

        if player_choice == "2":
            rng = random_number_game(name)
            rng()
        elif player_choice == "1":
            rps_play = rps(name)
            rps_play()
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
    