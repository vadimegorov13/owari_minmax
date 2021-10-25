# Min max functions are going to be stored here
from Node import Node
from copy import deepcopy


class MMABP():
    def get_heuristic(self, node):
        # need more stuff i think, idk, yeah
        computer_goal = node.state.board[6]
        human_goal = node.state.board[13]

        return computer_goal - human_goal

    def get_child(self, node):
        # It will get a legal move and than see if theres more legal moves left for the current states
        child = "child"
        has_more_children = True

        # add some code here

        return child, has_more_children

    # do_min and do_max will run recursively
    def do_min(self, node, alpha, beta, depth):
        # if the game is over on the last child it checks get's a heuristic for the child
        if node.state.game_over():
            node.set_heuristic(self.get_heuristic(node))
            return node

        # same as above but when it hits the max depth
        if depth == 0:
            node.set_heuristic(self.get_heuristic(node))
            return node

        # create a new node that will have the best result and then return it
        best_node = deepcopy(node)
        # assign +infinity to the heuristic of the best node
        best_node.set_heuristic(float('inf'))

        # add some cool stuff here

        # return best node with the best heuristic
        return best_node

    def do_max(self, node, alpha, beta, depth):
        # if the game is over on the last child it checks get's a heuristic for the child
        if node.state.game_over():
            node.set_heuristic(self.get_heuristic(node))
            return node

        # same as above but when it hits the max depth
        if depth == 0:
            node.set_heuristic(self.get_heuristic(node))
            return node

        # create a new node that will have the best result and then return it
        best_node = deepcopy(node)
        # assign -infinity to the heuristic of the best node
        best_node.set_heuristic(-float('inf'))

        # add some cool stuff here

        # return best node with the best heuristic
        return best_node

    def get_computer_move(self, ow):

        # parse a new node, -infinity alpha, +infinity beta and depth
        best_node = self.do_max(Node(ow), -float('inf'), float('inf'), 7)

        return best_node.move
