# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        n_right_deep = 1
        n_left_deep = 1
        if root.left:
            n_left_deep += self.maxDepth(root.left)
        if root.right:
            n_right_deep += self.maxDepth(root.right)
        if n_right_deep > n_left_deep:
            return n_right_deep
        else:
            return n_left_deep
