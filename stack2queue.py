"""
list index is -1 means the last value in list
use stack realizes queue
"""


class Queue:
    # initialize your data structure here.
    def __init__(self):
        self.stack = []

    # @param x, an integer
    # @return nothing
    def push(self, x):
        swap = []
        while self.stack:
            swap.append(self.stack.pop())
        swap.append(x)
        while swap:
            self.stack.append(swap.pop())

    # @return nothing
    def pop(self):
        self.stack.pop()

    # @return an integer
    def peek(self):
        return self.stack[-1]

    # @return an boolean
    def empty(self):
        return len(self.stack) == 0


if __name__ == '__main__':
    pass