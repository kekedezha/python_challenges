#number guessing game
import sys
import random

def random_number_game(name):
    game_count = 0
    player_wins = 0

    def play_game():
        nonlocal name
        nonlocal player_wins
        nonlocal game_count

        random_number = random.choice("123")
        player_choice = input(f"\n{name}, guess what number I am thinking of...1, 2 or 3.\n\n")

        # Check to ensure player has entered 1, 2 or 3
        if player_choice not in ["1", "2", "3"]:
            print(f"\n{name}, please enter 1, 2, or 3. ")
            return play_game()

        # List out what number the player chose and what correct number was
        if player_choice == random_number:
            player_wins += 1
            print(f"Congrats {name}! You correctly guessed the correct number!\n")
            print(f"\n{name} you chose {player_choice}.")
            print(f"I was thinking about the number {random_number}.\n")
            game_count += 1
        else:
            print(f"\n{name} you chose {player_choice}.")
            print(f"I was thinking about the number {random_number}.\n")
            print(f"Sorry {name}! You did not guess the correct number. Better luck next time.\n")
            game_count += 1

        # Print out game count, player wins and winning percentage per session
        print(f"Game count: {game_count}")
        print(f"{name}'s wins: {player_wins}")
        print(f"Your winning percentage is {(player_wins/game_count):0.2%}\n")

        # Ask player if they want to play again
        while True:
            play_again = input(f"Play again, {name}?\nY for Yes or\nQ to Quit\n")
            
            # Ensure player inputs 'y' for yes and 'q' for quit
            if play_again.lower() not in ["y","q"]:
                continue
            else:
                break

        # if player wants to play again, then run the play_game function again
        if play_again == "y":
            return play_game()
        # if player chose quit then thank them for playing
        else:
            print(f"Thank you for playing!")

            # if only running guess_number.py independently then exit file, else empty return to get out of function
            if __name__ == "__main__":
                sys.exit(f"Bye {name}!")
            else: 
                return

    return play_game

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

    rng = random_number_game(args.name);
    rng()