# CSCE A405 Assignment 3
# Authors: Vadim Egorov and Jared Vitug
# Update date: 10/25/2021

from Owari import Owari
from MMABP import MMABP


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


def play(ow):
    get_first_move(ow)

    print("\n~~~~~~Game started~~~~~~")
    ow.display_board()

    while True:
        if ow.turn == "north":
            # get human move
            ow.get_human_move()
            ow.display_board()
            # change turn
            ow.set_turn()
        else:
            # Create agent
            agent = MMABP()
            # get the best move
            pit = agent.get_computer_move(ow.board, ow.turn)
            ow.move(pit)
            print("\nComputer moved stones from pit ", pit)
            ow.display_board()
            # change turn
            ow.set_turn()

        if ow.game_over():
            print("\nGame Over!!!")
            ow.display_board()
            break

    if ow.board[6] == ow.board[13]:
        print("\n Tie!")
    elif ow.board[6] > ow.board[13]:
        print("\nSouth won!")
    else:
        print("\nNorth won!")


def main():
    # Test
    play(Owari())


if __name__ == "__main__":
    main()
