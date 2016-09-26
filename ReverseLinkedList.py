from .DataStructure.ListNode import ListNode
from .DataStructure.LinkedList import LinkedList


class ReverseLinkedList:
    def solution(self, head):
        """
        This method
        :param head: head is the head of a list
        :return: current_node
        """
        current_node = None
        while head:
            temp_node = head.next
            head.next = current_node
            current_node = head
            head = temp_node
        return current_node
