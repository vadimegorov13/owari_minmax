# Default board that gets initialized at the start of the game
DEF_BOARD = [3, 3, 3, 3, 3, 3, 0, 3, 3, 3, 3, 3, 3, 0]

# Dictionary of South player
#   - Contains a list of all possible moves and goal for SOUTH
SOUTH = {"pits": [0, 1, 2, 3, 4, 5], "goal": 6}

# Dictionary of North player
#   - Contains a list of all possible moves and goal for NORTH
NORTH = {"pits": [7, 8, 9, 10, 11, 12], "goal": 13}

# Dictionary of opposite pits
#   - Contains a list of all possible moves
OPPOSITE = {0: 12, 1: 11, 2: 10, 3: 9, 4: 8, 5: 7,
            12: 0, 11: 1, 10: 2, 9: 3, 8: 4, 7: 5}


class Owari:
    # Constructor
    def __init__(self):
        self.board = DEF_BOARD  # Assign defaul board
        self.turn = "north"     # Assign side of the first move

    # Switch turn using self.turn variable
    def set_turn(self):
        if self.turn == "north":
            self.turn = "south"
        else:
            self.turn = "north"

    # Get index of a pit from human and move
    def get_human_move(self):
        while True:
            if self.turn == "north":
                curr_pits = NORTH["pits"]
            else:
                curr_pits = SOUTH["pits"]

            pit = input(
                f"\nSpecify the pit from which you want to move stones {curr_pits}\n")

            pit = int(pit)

            if self.move_is_legal(pit) and curr_pits[0] <= pit <= curr_pits[5]:
                self.move(pit)
                print("\nYou moved stones from pit ", pit)
                break
            else:
                print("You don't have stones in this pit, please choose another one")

    # Check if pit is not empty
    # Move is legal (index of the pit): int => Boolean
    def move_is_legal(self, pit):
        if self.board[pit] == 0:
            return False

        return True

    # Moves stones from the chosen pit
    # Make a move (index of the pit): int => ()
    def move(self, pit):
        if self.turn == "north":
            curr_player = NORTH
            curr_opponent = SOUTH
        else:
            curr_player = SOUTH
            curr_opponent = NORTH

        # Take stones from the pit
        stones = self.board[pit]
        self.board[pit] = 0
        moving_stones = stones

        for _ in range(stones):
            # Check if we are on 13th pit then change pit to 0
            if pit == 13:
                pit = 0
            else:
                pit += 1

            if pit != curr_opponent["goal"]:
                self.board[pit] += 1
                moving_stones -= 1

                # Check if we can capture
                if self.board[pit] == 1 and pit in curr_player["pits"] and moving_stones == 0:
                    self.capture(pit, curr_player["goal"])

    # Capture opponents stones
    # Capture (index of the pit, index of the goal): int, int => ()
    def capture(self, pit, goal):
        # Add stones to curr_player goal
        self.board[goal] += self.board[OPPOSITE[pit]]
        # Empty the pit
        self.board[OPPOSITE[pit]] = 0

    # This function should be run after player made a move!
    # Checks if game is over
    # Game Over () => Boolean

    def game_over(self):
        player_empty = True
        opponent_empty = True

        if self.turn == "north":
            curr_player = NORTH
            curr_opponent = SOUTH
        else:
            curr_player = SOUTH
            curr_opponent = NORTH

        for i in range(curr_player["pits"][0], curr_player["pits"][5]+1):
            if self.board[i] != 0:
                player_empty = False

        for i in range(curr_opponent["pits"][0], curr_opponent["pits"][5]+1):
            if self.board[i] != 0:
                opponent_empty = False

        if player_empty:
            not_empty = curr_opponent
        elif opponent_empty:
            not_empty = curr_player
        else:
            return False

        for i in range(not_empty["pits"][0], not_empty["pits"][5]+1):
            # Add stones to the goal
            self.board[not_empty["goal"]] += self.board[i]
            # Empty the pit
            self.board[i] = 0

        return True

    # Display board
    def display_board(self):

        # North pits
        print("    ", end="")
        for i in range(12, 6, -1):
            print(self.board[i], end="  ")

        # Goals
        print("\n", self.board[13], "                  ", self.board[6])

        # South pits
        print("\n    ", end="")
        for i in range(0, 6, 1):
            print(self.board[i], end="  ")

        # end with new blank line
        print("")
