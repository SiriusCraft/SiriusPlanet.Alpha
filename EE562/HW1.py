"""
Count how many states are searched to find each solution; there are four.
For your counting keep track of 3 kinds of states you generate:
illegal states in which the cannibals eat the missionaries,
repeated states that are the same as an ancestor state on the same path,
total states searched (ie. all states except the illegal and repeated ones).

the solutions your program finds, each solution being an ordered
list of states from initial state to goal state. Format as follows:
(3,3,L)(3,1,R)(3,2,L)...(0,0,R)

The 3 counts: illegal count, repeat count, total count for each solution.
"""


class State:
    """
    This class is the state in Missionaries and Cannibals
    problem.
    """

    def __init__(self, missionaries, cannibals, boat):
        """
        This is an initial method
        :param missionaries: missionaries on the left bank
        :param cannibals: cannibals on the left bank
        :param boat: R means boat on the right bank, L means left
        """
        self.missionaries = missionaries
        self.cannibals = cannibals
        self.missionaries_right = 3 - missionaries
        self.cannibals_right = 3 - cannibals
        self.boat = boat
        self.parent = None
        self.repeated_count = 0
        self.state_format = '({0},{1},{2})'

    def is_goal(self):
        """
        This method checks if current state reaches goal
        :return: Boolean
        """
        if self.missionaries is 0 and self.cannibals is 0 and self.boat is 'R':
            return True
        else:
            return False

    def is_legal(self):
        """
        **********************repeat and illegal count*****************
        :return:
        """
        if self.boat in {'L', 'R'} and 0 <= self.missionaries <= 3 and 0 <= self.cannibals <= 3 \
                and (self.missionaries is 0 or self.missionaries >= self.cannibals) \
                and (self.missionaries_right is 0 or self.missionaries_right >= self.cannibals_right):
            return True
        else:
            return False

    def is_discovered(self, discovered_states):
        """
        This method checks if state has been discovered
        before. If so, return False or else add it to
        discovered states set.
        :param discovered_states: a set contains states discovered
        :return: Boolean
        """
        if (self.missionaries, self.cannibals, self.boat) in discovered_states:
            print('repeat')
            return False
        else:
            discovered_states.add((self.missionaries, self.cannibals, self.boat))
            return True

    @staticmethod
    def successors(current_state):
        """
        This static method add legal successor states to list children
        :param current_state: current state
        :return:children is a list that contains legal successor states
        """
        children = []
        if current_state.missionaries is 0 and current_state.cannibals is 0 and current_state.boat is 'R':
            print("**&*&*&*&*")
            children = []
        elif current_state.boat is 'L':
            # 2 cannibals from left to right
            new_state = State(current_state.missionaries, current_state.cannibals - 2, 'R')
            State.operate_legal_state(new_state, current_state, children)
            # 2 missionaries from left to right
            new_state = State(current_state.missionaries - 2, current_state.cannibals, 'R')
            State.operate_legal_state(new_state, current_state, children)
            # 1 missionary and 1 cannibal from left to right
            new_state = State(current_state.missionaries - 1, current_state.cannibals - 1, 'R')
            State.operate_legal_state(new_state, current_state, children)
            # 1 missionary from left to right
            new_state = State(current_state.missionaries - 1, current_state.cannibals, 'R')
            State.operate_legal_state(new_state, current_state, children)
            # 1 cannibal from left to right
            new_state = State(current_state.missionaries, current_state.cannibals - 1, 'R')
            State.operate_legal_state(new_state, current_state, children)
        elif current_state.boat is 'R':
            print("use this")
            # 2 cannibals from right to left
            new_state = State(current_state.missionaries, current_state.cannibals + 2, 'L')
            State.operate_legal_state(new_state, current_state, children)
            # 2 missionaries from right to left
            new_state = State(current_state.missionaries + 2, current_state.cannibals, 'L')
            State.operate_legal_state(new_state, current_state, children)
            # 1 missionary and 1 cannibal from right to left
            new_state = State(current_state.missionaries + 1, current_state.cannibals + 1, 'L')
            State.operate_legal_state(new_state, current_state, children)
            # 1 missionary from right to left
            new_state = State(current_state.missionaries + 1, current_state.cannibals, 'L')
            State.operate_legal_state(new_state, current_state, children)
            # 1 cannibal from right to left
            new_state = State(current_state.missionaries, current_state.cannibals + 1, 'L')
            State.operate_legal_state(new_state, current_state, children)
        return children

    @staticmethod
    def operate_legal_state(new_state, current_state, children):
        """
        This static method checks if new state is legal then
        make current state parent of legal state and append it
        to list of children
        :param new_state:
        :param current_state:
        :param children:
        :return:
        """
        if new_state.is_legal():
            new_state.parent = current_state
            children.append(new_state)

    @staticmethod
    def DFS(current_state, discovered_states):
        current_state.is_discovered(discovered_states)
        for s in State.successors(current_state):
            print(s.state_format.format(current_state.missionaries, current_state.cannibals, current_state.boat))
            # current_state = s
            while s.is_discovered(discovered_states):
                # print("m:{0}, c:{1}, b:{2}, pm:{3},pc:{4},pb:{5}".format(s.missionaries, s.cannibals, s.boat,
                # s.parent.missionaries, s.parent.cannibals,
                # s.parent.boat))
                s.parent = current_state
                current_state = s
                print(s.state_format.format(current_state.missionaries, current_state.cannibals, current_state.boat))
                if s.is_goal():
                    print('~~~~~~~~~~~~~~finish~~~~~~~~~~~~~~')
                    print('-----@@@@{0}'.format(s))
                    return s
                else:
                    State.DFS(current_state, discovered_states)

    @staticmethod
    def solution():
        discovered_states = set()
        initial_state = State(3, 3, 'L')
        progress = []
        progress.append(initial_state)
        # repeated_count = 0
        # print(progress[0])
        final = State.DFS(initial_state, discovered_states)
        # print(type(final))
        # print(State(0,0,'L').state_format.format(final.missionries, final.cannibals, final.boat))


if __name__ == '__main__':
    # print(State.successors(State(0,0,'R')))
    State.solution()
    # s = State(3, 1, 'R')
    # e = set()
    # s0 = State(3, 3, 'L')
    # repeated_count = 0
    # s0.is_discovered(e)
    # print(e)
    # print("_______")
    # # print(s.parent() == s)
    # # print(s.is_goal())
    # for n in s.successors(s):
    #     n.is_discovered(e)
    # print(repeated_count)
    # print(e)
    # else:
    #     print("m:{0}, c:{1}, b:{2}, pm:{3},pc:{4},pb:{5}".format(n.missionaries, n.cannibals, n.boat, n.parent.missionaries, n.parent.cannibals, n.parent.boat))
