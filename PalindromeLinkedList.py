from DataStructure.ListNode import ListNode
from DataStructure.LinkedList import LinkedList


class Solution(object):
    @staticmethod
    def is_palindrome(head):
        """
        :type head: ListNode
        :rtype: bool
        """
        is_palindrome_list = LinkedList(head)
        second_half_list = LinkedList(is_palindrome_list.find_mid_node())
        reversed_second_half_list = LinkedList(second_half_list.reverse_list())
        print(Solution().compare_two_list(reversed_second_half_list, is_palindrome_list))

    @staticmethod
    def compare_two_list(list1, list2):
        current1 = list1.head
        current2 = list2.head
        while current1 and current2:
            try:
                if current1.val == current2.val:
                    flag = True
                else:
                    flag = False
                current1 = current1.next
                current2 = current2.next
            except AttributeError:
                flag = False
                break
        return flag


if __name__ == '__main__':
    list1 = LinkedList.test_list()
    Solution().is_palindrome(list1.head)
