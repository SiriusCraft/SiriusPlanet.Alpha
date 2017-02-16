from DataStructure.ListNode import ListNode


class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return False
        fast = slow = head
        while fast.next and fast.next.next:
            if not fast.next:
                return False
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                return True
        return False


if __name__ == '__main__':
    pass
