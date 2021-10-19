# CSCE A405 Assignment 3
# Authors: Vadim Egorov and Jared Vitug
# Update date: 10/21/2021

from Owari import Owari


# Decide who is going first
def get_first_move():
    while True:
        first_move = input(
            "Do you want to move first? (Enter: Yes/No, y/n) \n")

        if first_move.lower() == "yes" or first_move.lower() == "y":
            print("North moves first!")
            return "north"
        elif first_move.lower() == "no" or first_move.lower() == "n":
            print("South moves first!")
            return "south"


def main():
    # Test
    ow = Owari()

    turn = get_first_move()

    print("\n~~~~~~~~~Game started!~~~~~~~~~")
    ow.display_board()

    while True:
        ow.get_human_move(turn)
        ow.display_board()
        if ow.game_over(turn):
            print("\nGame Over!!!")
            break

        if turn == "north":
            turn = "south"
        else:
            turn = "north"

    ow.display_board()

    if ow.board[6] > ow.board[13]:
        print("South won!")
    else:
        print("North won!")


if __name__ == "__main__":
    main()
