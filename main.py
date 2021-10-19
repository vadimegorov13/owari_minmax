# CSCE A405 Assignment 3
# Authors: Vadim Egorov and Jared Vitug
# Update date: 10/21/2021

from Owari import Owari
from time import perf_counter


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


def main():
    # Test
    ow = Owari()

    get_first_move(ow)

    print("\n~~~~~~Game started~~~~~~")
    ow.display_board()

    while True:
        ow.get_human_move()
        ow.display_board()

        if ow.game_over():
            print("\nGame Over!!!")
            break

        ow.set_turn()


    ow.display_board()

    if ow.board[6] > ow.board[13]:
        print("\nSouth won!")
    else:
        print("\nNorth won!")


if __name__ == "__main__":
    main()
