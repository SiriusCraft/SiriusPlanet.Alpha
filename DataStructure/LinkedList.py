"""
This module includes LinkedList class, which is a singly
linked list with functional methods.
"""
from DataStructure.ListNode import ListNode


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
        temp_node = self.head
        self.head = new_node
        self.head.next = temp_node

    def len(self):
        """
        This method return length of list
        :return: list_len
        """
        current = self.head
        list_len = 0
        while current:
            list_len += 1
            current = current.next
        return list_len

    @staticmethod
    def generate_test_list(list_len):
        """
        This method return the head of list
        with a given list length
        :param list_len: length of generated list
        :return:
        """
        temp_head = None
        test_list = LinkedList(temp_head)
        for i in range(list_len):
            test_list.insert_node(i)
        return test_list.head

    def reverse_list(self):
        """
        This method reverse a list and return head
        of new list
        :return: crt
        """
        crt = None
        head = self.head
        while head:
            temp = head.next
            head.next = crt
            crt = head
            head = temp
        return crt

    def print_list(self):
        """
        This method print nodes of list
        :return: None
        """
        current = self.head
        while current:
            print("{0}".format(current.val))
            current = current.next

    @staticmethod
    def test_list():
        """
        This method returns a test list
        :return: test_list
        """
        node5 = ListNode(1, None)
        node4 = ListNode(2, node5)
        node3 = ListNode(9, node4)
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
        if not self.head:
            return self.head
        else:
            fast_pointer = self.head
            slow_pointer = self.head
            while fast_pointer.next and fast_pointer.next.next:
                fast_pointer = fast_pointer.next.next
                slow_pointer = slow_pointer.next
            mid_pointer = slow_pointer
            return mid_pointer


if __name__ == '__main__':
    pass
