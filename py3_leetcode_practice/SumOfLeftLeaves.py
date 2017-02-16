# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def sum(root, flag):
            if not root:
                return 0
            if flag and not root.left and not root.right:
                return root.val
            return sum(root.left, True) + sum(root.right, False)

        return sum(root.left, True) + sum(root.right, False)
