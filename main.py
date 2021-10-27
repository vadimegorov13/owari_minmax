# CSCE A405 Assignment 3
# Authors: Vadim Egorov and Jared Vitug
# Update date: 10/25/2021

from Owari import Owari
from MMABP import MMABP
from copy import deepcopy


# Decide who is going first
def get_first_move(ow):
    while True:
        first_move = input(
            "Do you want to move first? (Enter: Yes/No, y/n) \n")

        if first_move.lower() == "yes" or first_move.lower() == "y":
            print("\nNorth moves first!")
            break
        elif first_move.lower() == "no" or first_move.lower() == "n":
            print("\nSouth moves first!")
            ow.set_turn()
            break

# Play a game with computer
def human_vs_computer(ow, depth):
    # Decide who is going first
    get_first_move(ow)

    print("\n              GAME STARTED")
    ow.display_board()

    while True:
        if ow.turn == "north":
            # Make human move
            ow.get_human_move()
            ow.display_board()
            # Change turn
            ow.set_turn()
        else:
            # Get the best move
            pit = MMABP().get_computer_move(deepcopy(ow.board), deepcopy(ow.turn), depth)
            # Make a computer move
            ow.move(pit)
            ow.display_board()
            # change turn
            ow.set_turn()

        # Check if game is over
        if ow.game_over():
            print("\nGame Over!!!")
            ow.display_board()
            break

    # Decide a winner
    if ow.board[6] == ow.board[13]:
        print("\n Tie!")
    elif ow.board[6] > ow.board[13]:
        print("\nSouth won!")
    else:
        print("\nNorth won!")

def human_vs_human(ow):
    get_first_move(ow)
    print("\n              GAME STARTED")
    ow.display_board()

    while True:
        # Make human move
        ow.get_human_move()
        ow.display_board()
        # Change turn
        ow.set_turn()

        # Check if game is over
        if ow.game_over():
            print("\nGame Over!!!")
            ow.display_board()
            break

    # Decide a winner
    if ow.board[6] == ow.board[13]:
        print("\n Tie!")
    elif ow.board[6] > ow.board[13]:
        print("\nSouth won!")
    else:
        print("\nNorth won!")


def main():
    depth = 10
    # Start a game
    human_vs_computer(Owari(), depth)
    # human_vs_human(Owari())


if __name__ == "__main__":
    main()
