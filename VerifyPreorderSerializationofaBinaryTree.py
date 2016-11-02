"""
Verify Preorder Serialization of a Binary Tree
https://www.hrwhisper.me/leetcode-verify-preorder-serialization-of-a-binary-tree/
tip:
len(stack) >= 3 and stack[-3] != '#'
the order cannot be wrong 
"""


class Solution(object):
    def isValidSerialization(self, preorder):
        """
        :type preorder: str
        :rtype: bool
        """
        preorder_list = preorder.split(",")
        stack = []
        for x in preorder_list:
            stack.append(x)
            while stack[-2:] == ['#', '#'] and len(stack) >= 3 and stack[-3] != '#':
                stack.pop()
                stack.pop()
                stack.pop()
                stack.append('#')
        return stack == ["#"]


if __name__ == '__main__':
    s = Solution()
    print(s.isValidSerialization("#"))
