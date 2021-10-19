# Saves the state of the game

# state = Owari()
# heuristic = heuristic value of the satte
# children = array of chidrens of this state
# move = shows which pit was moved on to get to that state

class Node:
    def __init__(self, state):
        self.state = state
        self.heuristic = 0
        self.children = []
        self.move = -1

    def set_num(self, num):
        self.num = num

    def set_heuristic(self, heuristic):
        self.heuristic = heuristic

    def set_children(self, children):
        self.children = children

    def set_move(self, move):
        self.move = move

    