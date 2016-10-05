class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if not head:
            return None
        fast = slow = head
        while fast.next and fast.next.next:
            if not fast.next:
                return None
            fast = fast.next.next
            slow = slow.next
            if fast == slow:
                z = fast
                p1 = head
                p2 = z
                while True:
                    if p1 == p2:
                        return p1
                    p1 = p1.next
                    p2 = p2.next
        return None

if __name__ == '__main__':
    pass
