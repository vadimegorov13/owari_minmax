# Min max functions are going to be stored here
from copy import deepcopy
from Owari import NORTH, SOUTH, OPPOSITE


class MMABP():
    # Moves stones from the chosen pit
    # Make a move (board, turn, index of the pit): arr, string, int => ()
    def move(self, board, turn, pit):
        if turn == "north":
            curr_player = NORTH
            curr_opponent = SOUTH
        else:
            curr_player = SOUTH
            curr_opponent = NORTH

        # Take stones from the pit
        stones = board[pit]
        board[pit] = 0
        moving_stones = stones

        for _ in range(stones):
            # Check if we are on 13th pit then change pit to 0
            if pit == 13:
                pit = 0
            else:
                pit += 1

            if pit != curr_opponent["goal"]:
                board[pit] += 1
                moving_stones -= 1

                # Check if we can capture
                if board[pit] == 1 and pit in curr_player["pits"] and moving_stones == 0:
                    board = self.capture(board, pit, curr_player["goal"])

        return board

    # Capture opponents stones
    # Capture (board, index of the pit, index of the goal): arr, int, int => ()
    def capture(self, board, pit, goal):
        # Add stones to curr_player goal
        board[goal] += board[OPPOSITE[pit]]
        # Empty the pit
        board[OPPOSITE[pit]] = 0

        return board

    # Check if game is over

    def game_over(self, board):
        north_empty = True
        south_empty = True

        for i in range(NORTH["pits"][0], NORTH["pits"][5]+1):
            if board[i] != 0:
                north_empty = False

        for i in range(SOUTH["pits"][0], SOUTH["pits"][5]+1):
            if board[i] != 0:
                south_empty = False

        if north_empty or south_empty:
            return True

        return False

    # Get final score of the game

    def final_score(self, board):
        human_goal = 0
        computer_goal = 0

        for i in range(NORTH["pits"][0], NORTH["pits"][5]+1):
            # Add stones to the goal
            human_goal += board[i]
        for i in range(SOUTH["pits"][0], SOUTH["pits"][5]+1):
            # Add stones to the goal
            computer_goal += board[i]

        return computer_goal - human_goal

    # Get heuristic of the move
    def get_heuristic(self, board):
        computer_goal = board[6]
        human_goal = board[13]

        heuristic = computer_goal - human_goal

        return heuristic

    # Check if pit is not empty
    # Move is legal (board, index of the pit): int => Boolean
    def move_is_legal(self, board, pit):
        if board[pit] == 0:
            return False

        return True

    # Get all legal moves for the current state
    def get_moves(self, board, turn):
        # Init move list
        move_list = []

        # Check which side should move
        if turn == "north":
            side = NORTH
        else:
            side = SOUTH

        # Iterate through each playable pit
        for i in side["pits"]:
            # Check if move is legal
            new_board = deepcopy(board)
            if self.move_is_legal(new_board, i) and side["pits"][0] <= i <= side["pits"][5]:
                # Append current move to the list
                move_list.append(i)

        return move_list


    def minimax(self, board, turn, alpha, beta, depth):
        best_heuristic = 0
        best_move = -1

        if depth == 0:
            best_heuristic = self.get_heuristic(board)
            return best_move, best_heuristic

        elif self.game_over(board):
            best_heuristic = self.final_score(board)
            return best_move, best_heuristic

        elif turn == "south":
            best_heuristic = -float('inf')
            for move in self.get_moves(deepcopy(board), turn):
                updated_board = self.move(deepcopy(board), turn, move)

                _, heuristic = self.minimax(
                    deepcopy(updated_board), "north", alpha, beta, depth-1)

                if heuristic > best_heuristic:
                    best_heuristic = heuristic
                    best_move = move

                alpha = max(alpha, best_heuristic)

                # prune
                if best_heuristic >= beta:
                    break
        else:
            best_heuristic = float('inf')
            for move in self.get_moves(deepcopy(board), turn):
                updated_board = self.move(deepcopy(board), turn, move)

                _, heuristic = self.minimax(
                    deepcopy(updated_board), "south", alpha, beta, depth-1)

                if heuristic < best_heuristic:
                    best_heuristic = heuristic
                    best_move = move

                beta = min(beta, best_heuristic)

                # prune dat shit
                if best_heuristic <= alpha:
                    break

        # Return best move and heuristic of the current state
        return best_move, best_heuristic

    # This function will be called from main()
    # get_computer_move(board: int array, turn: string) => best_move: int
    def get_computer_move(self, board, turn):

        best_move, _ = self.minimax(
            board, turn, -float('inf'), float('inf'), 10)

        # print(f"heuristic of the move: {heuristic}")

        return best_move
