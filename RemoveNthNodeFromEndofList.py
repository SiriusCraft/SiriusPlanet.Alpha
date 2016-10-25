"""
These tips seems to be useful...
TL;DR
1. 越界：容易造成内存访问错误，比如调用了NULL->next。尤其对于空链表的特殊情况。
2. 更新head的特殊处理
3. 删除节点时没有保留下一个移动位置的指针（多用于reverse linked list）。
4. 移动位置存在+-1的偏差。
5. 链表题多用指针操作。注意指针作为函数参数时是pass by value： f(ListNode *p)，还是pass by reference：f(ListNode *&p)

常用技巧：
1. Dummy head：简化改变、删除头指针的处理。
2. 前后双指针：多用于链表反转。
"""
# Definition for singly-linked list.
from DataStructure.ListNode import ListNode
from DataStructure.LinkedList import LinkedList


class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head == None:
            return []
        count_down = n
        dummy = ListNode(0)
        dummy.next = head
        pointer1 = pointer2 = dummy
        pointer2_previous = dummy
        while pointer1.next:
            count_down -= 1
            if count_down < 1:
                pointer2_previous = pointer2
                pointer2 = pointer2.next
            pointer1 = pointer1.next
        pointer2_previous.next = pointer2.next
        return dummy.next


if __name__ == '__main__':
    l = LinkedList(LinkedList(ListNode(1)).generate_test_list(1))
    s = Solution()
    head = s.removeNthFromEnd(l.head, 1)
    LinkedList(head).print_list()
