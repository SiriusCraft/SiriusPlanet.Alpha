"""
Last update: 2016-10-10 21:45
Maintainer: Cunzhi Ren <renc@uw.edu>
Environment: python 3.5.2
HomeWork1 of EE562 Artificial Intelligence for Engineers:
Missionary-Cannibal Problem (with 3 missionaries and 3 cannibals)
with a RECURSIVE DEPTH-FIRST SEARCH
"""


class State:
    """
    This class is the state in Missionaries and Cannibals
    problem.
    """

    def __init__(self, missionaries, cannibals, boat):
        """
        This is an initial method.
        :param missionaries: missionaries on the left bank
        :param cannibals: cannibals on the left bank
        :param boat: R means boat on the right bank, L means left
        """
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.missionaries_right = 3 - missionaries
        self.cannibals_right = 3 - cannibals
        self.boat = boat

    def is_goal(self):
        """
        This method checks if current state reaches goal. If state reaches
        goal then return true, else return false.
        :return: Boolean
        """
        return not self.missionaries and not self.cannibals and self.boat is 'R'

    def is_legal(self):
        """
        This method checks if a state is legal. If not legal, illegal count
        plus 1.
        :return: Boolean
        """
        global illegal_count
        if (self.missionaries_right is 0 or self.missionaries_right >= self.cannibals_right) \
                and self.boat in {'L', 'R'} and 0 <= self.missionaries <= 3 \
                and 0 <= self.cannibals <= 3 \
                and (self.missionaries is 0 or self.missionaries >= self.cannibals):
            return True
        else:
            illegal_count += 1
            return False

    def is_discovered(self, progress):
        """
        This method checks if state has been discovered
        before. If so, return False or else add it to
        discovered states set.
        :param progress: a list contains states used before
        :return: Boolean
        """
        global repeat_count
        if (self.missionaries, self.cannibals, self.boat) in progress:
            return True
        else:
            repeat_count += 1
            return False

    @staticmethod
    def successors(current_state):
        """
        This static method add legal successor states to list children
        :param current_state: current state
        :return:children
        """
        children = []
        if current_state.boat is 'L':
            # 2 cannibals from left to right
            new_state = State(current_state.missionaries, current_state.cannibals - 2, 'R')
            State.operate_legal_state(new_state, children)
            # 2 missionaries from left to right
            new_state = State(current_state.missionaries - 2, current_state.cannibals, 'R')
            State.operate_legal_state(new_state, children)
            # 1 missionary and 1 cannibal from left to right
            new_state = State(current_state.missionaries - 1, current_state.cannibals - 1, 'R')
            State.operate_legal_state(new_state, children)
            # 1 missionary from left to right
            new_state = State(current_state.missionaries - 1, current_state.cannibals, 'R')
            State.operate_legal_state(new_state, children)
            # 1 cannibal from left to right
            new_state = State(current_state.missionaries, current_state.cannibals - 1, 'R')
            State.operate_legal_state(new_state, children)
        if current_state.boat is 'R':
            # 2 cannibals from right to left
            new_state = State(current_state.missionaries, current_state.cannibals + 2, 'L')
            State.operate_legal_state(new_state, children)
            # 2 missionaries from right to left
            new_state = State(current_state.missionaries + 2, current_state.cannibals, 'L')
            State.operate_legal_state(new_state, children)
            # 1 missionary and 1 cannibal from right to left
            new_state = State(current_state.missionaries + 1, current_state.cannibals + 1, 'L')
            State.operate_legal_state(new_state, children)
            # 1 missionary from right to left
            new_state = State(current_state.missionaries + 1, current_state.cannibals, 'L')
            State.operate_legal_state(new_state, children)
            # 1 cannibal from right to left
            new_state = State(current_state.missionaries, current_state.cannibals + 1, 'L')
            State.operate_legal_state(new_state, children)
        return children

    @staticmethod
    def operate_legal_state(new_state, children):
        """
        This static method checks if new state is legal then
        make current state parent of legal state and append it
        to list of children
        :param new_state: possible successor state of current state
        :param children: a list contains contains legal successor states
        :return: None
        """
        if new_state.is_legal():
            children.append(new_state)

    @staticmethod
    def dfs(current_state, progress):
        """
        This static method implements Depth First Search recursively
        generate progress from initial state to goal state
        and keeps all the progresses in solutions.
        :param current_state: current state implemented DFS
        :param progress: the progress from initial state to goal
        :return: None
        """
        if current_state.is_goal():
            progress.append((current_state.missionaries, current_state.cannibals, current_state.boat))
            global total_count
            total_count += 1
            solutions.append(progress[:])
            progress.remove((current_state.missionaries, current_state.cannibals, current_state.boat))
            return
        if current_state.is_discovered(progress):
            return
        children = State.successors(current_state)
        progress.append((current_state.missionaries, current_state.cannibals, current_state.boat))
        total_count += 1
        for child in children:
            State.dfs(child, progress)
        progress.remove((current_state.missionaries, current_state.cannibals, current_state.boat))

    @staticmethod
    def solution():
        """
        This static method sets some initial values for problem,
        solves Missionaries and Cannibals problem and prints solutions
        with total, illegal, repeat counts.
        :return: None
        """
        global repeat_count, illegal_count, total_count, solutions
        repeat_count = 1
        total_count = 0
        illegal_count = 0
        relunctant_illegal = 40
        solutions = []
        initial_state = State(3, 3, 'L')
        progress = []
        State.dfs(initial_state, progress)
        for index, state in enumerate(solutions):
            print("Solution{0}:".format(index + 1))
            for state in solutions[index]:
                print("{0}".format(state))
        print("totals {0} illegals {1} repeats {2}".format(total_count,
                                                           illegal_count - relunctant_illegal, repeat_count))


if __name__ == '__main__':
    State.solution()
