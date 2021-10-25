# Saves the state of the game

# state = Owari() board and turn
# heuristic = heuristic value of the state
# children = array of chidrens of this state
# move = shows which pit was moved to get to that state

class Node:
    def __init__(self, state):
        self.state = state
        self.heuristic = 0
        self.children = []
        self.move = -1

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def set_children(self, children):
        self.children = children

    def set_move(self, move):
        self.move = move
