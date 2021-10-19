DEF_BOARD = [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0]
# Dictionary of South player
SOUTH = {"pits": [0, 1, 2, 3, 4, 5], "goal": 6}
# Dictionary of North player
NORTH = {"pits": [7, 8, 9, 10, 11, 12], "goal": 13}
# Dictionary of opposite pits
OPPOSITE = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7,
            12: 0, 11: 1, 10: 2, 9: 3, 8: 4, 7: 5}


class Owari:
    # Constructor
    def __init__(self, board=DEF_BOARD):
        self.board = board

    # Get index of a pit from human and move
    def get_human_move(self, turn):
        while True:
            if turn == "north":
                pit = input(
                    "\nSpecify the pit from which you want to move stones (7, 8, 9, 10, 11, or 12) \n")

                pit = int(pit)

                if self.move_is_legal(pit) and 7 <= pit <= 12:
                    print("You moved stones from pit ", pit)
                    self.move(pit)
                    return

            elif turn == "south":
                pit = input(
                    "\nSpecify the pit from which you want to move stones (0, 1, 2, 3, 4, or 5) \n")

                pit = int(pit)

                if self.move_is_legal(pit) and 0 <= pit <= 5:
                    print("You moved stones from pit ", pit)
                    self.move(pit)
                    return

    # Check if pit is not empty
    def move_is_legal(self, pit):
        if self.board[pit] == 0:
            print("You don't have stones in this pit, please choose another one")
            return False

        return True

    # Moves stones from the chosen pit
    # Make a move (index of the pit) => ()
    def move(self, pit):
        curr_player = None
        curr_opponent = None

        if pit in SOUTH["pits"]:
            curr_player = SOUTH
            curr_opponent = NORTH
        else:
            curr_player = NORTH
            curr_opponent = SOUTH

        # Take stones from the pit
        stones = self.board[pit]
        self.board[pit] = 0

        for _ in range(stones):
            # Check if we are on 13th pit then change pit to 0
            if pit == 13:
                pit = 0
            else:
                pit += 1

            if pit != curr_opponent["goal"]:
                self.board[pit] += 1

                # Check if we can capture
                if self.board[pit] == 1 and pit in curr_player["pits"]:
                    self.capture(pit, curr_player["goal"])

    # Capture opponents stones
    # Capture (index of the pit, index of the goal) => ()
    def capture(self, pit, goal):
        # Take stones from opponent
        stones = self.board[OPPOSITE[pit]]
        self.board[OPPOSITE[pit]] = 0

        # Add stones to curr_player goal
        self.board[goal] += stones

    # Display board
    def display_board(self):

        # South pits
        print("\n    ", end='')
        for i in range(5, -1, -1):
            print(self.board[i], end="  ")

        # Goals
        print("\n", self.board[6], "                  ", self.board[13])

        # North pits
        print("    ", end='')
        for i in range(7, 13):
            print(self.board[i], end="  ")

        # end with new blank line
        print('')

    # This function should be run after player made a move!
    # Checks if game is over
    # Game Over (North or South) => Boolean
    def game_over(self, curr_turn):
        curr_player = None
        curr_opponent = None

        if curr_turn == "north":
            curr_player = NORTH
            curr_opponent = SOUTH
        else:
            curr_player = SOUTH
            curr_opponent = NORTH

        for i in range(curr_player["pits"][0], curr_player["pits"][5]+1):
            if self.board[i] != 0:
                return False

        for i in range(curr_opponent["pits"][0], curr_opponent["pits"][5]+1):
            # Take stones from the pit
            stones = self.board[i]
            self.board[i] = 0

            # Add stones to the goal
            self.board[curr_opponent["goal"]] += stones

        return True
