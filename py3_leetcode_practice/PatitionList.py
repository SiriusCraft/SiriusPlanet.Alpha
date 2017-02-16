"""
head small contains node whoes val is small than x
head big contains node whoes val is greater than or equal to x
"""
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        if not head:
            return []
        small_head = ListNode(0)
        big_head = ListNode(0)
        small_dummy = small_head
        big_dummy = big_head
        current = head
        while current:
            if current.val < x:
                small_head.next = current
                small_head = current
            if current.val >= x:
                big_head.next = current
                big_head = current
            current = current.next
        small_head.next = None
        big_head.next = None
        dummy = small_dummy
        while small_dummy.next:
            small_dummy = small_dummy.next
        small_dummy.next = big_dummy.next
        return dummy.next


# if __name__ == '__main__':
#     head = ListNode(1)
#     # head.next = ListNode(3)
#     # head.next.next = ListNode(2)
#     # head.next.next.next = ListNode(4)
#     s = Solution()
#     s.partition(head, 0)
