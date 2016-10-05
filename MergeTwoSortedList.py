"""
You have to use result.next = l1 or l2
or else you will lose the condition that
dummy.next = result, thus you will lose
the head of list
"""
from DataStructure.ListNode import ListNode


class Solution(object):
    @staticmethod
    def merge_two_lists(l1, l2):
        """
        This method splices two sorted lists
        together hence creates a new merged sorted list.
        :type l1: ListNode
        :type l2: ListNode
        :rtype dummy.next: ListNode
        """
        dummy = ListNode(0)
        result = dummy
        while l1 and l2:
            if l1.val > l2.val:
                result.next = l2
                l2 = l2.next
            else:
                result.next = l1
                l1 = l1.next
            result = result.next
        if not l1:
            result.next = l2
        if not l2:
            result.next = l1
        return dummy.next
