"""
ListNode is a class of list node for singly linked
list.
"""


class ListNode(object):
    def __init__(self, x, next=None):
        self.val = x
        self.next = next
