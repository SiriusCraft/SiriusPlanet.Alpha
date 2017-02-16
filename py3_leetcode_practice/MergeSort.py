"""
LeetCode 148 Sort List
"""
from DataStructure.ListNode import ListNode


class Solution(object):
    def sortList(self, head):
        """
        This method merge sorts Linked lists
        in O(nlogn) time
        :type head: ListNode
        :rtype head : ListNode
        """
        if not head or not head.next:
            return head
        if not head:
            return head
        else:
            fast_pointer = head
            slow_pointer = head
            while fast_pointer.next and fast_pointer.next.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            mid_pointer = slow_pointer.next
            slow_pointer.next = None
            list_a = head
            list_b = mid_pointer
        list_a = self.sortList(list_a)
        list_b = self.sortList(list_b)
        head = self.merge_sorted_lists(list_a, list_b)
        return head

    def merge_sorted_lists(self, list_a, list_b):
        dummy = ListNode(0)
        result = dummy
        while list_a and list_b:
            if list_a.val > list_b.val:
                result.next = list_b
                list_b = list_b.next
            else:
                result.next = list_a
                list_a = list_a.next
            result = result.next
        if not list_a:
            result.next = list_b
        if not list_b:
            result.next = list_a
        return dummy.next
