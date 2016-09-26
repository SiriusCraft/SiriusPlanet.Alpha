from .ListNode import ListNode

"""

"""


class LinkedList:
    """
    This class is a singly linked list.
    """

    def __init__(self, head):
        self.head = head

    def insert_node(self, data):
        """
        This method insert new node to list by place new node
        at the head of list and point the new node at the old
        head.
        """
        new_node = ListNode(data)
        self.head = new_node

    def sizeof(self):
        current = self.head
        size = 0
        while current:
            size += 1
            current = current.next_node
        return size

    @staticmethod
    def generate_test_list(list_len):
        i = 0
        head = ListNode(i)
        test_list = LinkedList(head)
        for i in range(0, list_len):
            test_list.insert_node(i)
        return head

    def reverse_list(self):
        crt = None
        head = self.head
        while head:
            temp = head.next
            head.next = crt
            crt = head
            head = temp
        return crt

    def print_list(self):
        current = self.head
        while current:
            print("{0}".format(current.val))
            current = current.next

    @staticmethod
    def test_list():
        node5 = ListNode(1, None)
        node4 = ListNode(2, node5)
        node3 = ListNode(1, node4)
        node2 = ListNode(2, node3)
        node1 = ListNode(1, node2)
        test_list = LinkedList(node1)
        return test_list

    def find_mid_node(self):
        """
        This method finds the middle node of a list
        :param head: the head of list
        :return: mid_node
        """
        if not self.head.next:
            return self.head
        else:
            current_node = self.head
            fast_pointer = current_node.next
            slow_pointer = current_node
            while fast_pointer.next:
                fast_pointer = fast_pointer.next
                slow_pointer = slow_pointer.next
            mid_pointer = slow_pointer
            return mid_pointer


if __name__ == '__main__':
    node = ListNode(1, None)
