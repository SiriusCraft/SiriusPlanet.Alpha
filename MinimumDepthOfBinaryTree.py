# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0
        n_right_deep = 1
        n_left_deep = 1
        if not root.left and not root.right:
            return 1
        if root.left:
            n_left_deep += self.minDepth(root.left)
        if root.right:
            n_right_deep += self.minDepth(root.right)
        if n_right_deep ==1:
            return  n_left_deep
        if n_left_deep == 1:
            return  n_right_deep
        if n_right_deep <= n_left_deep:
            return n_right_deep
        if n_right_deep > n_left_deep:
            return n_left_deep


if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(1)
    root.right = TreeNode(1)
    s = Solution()
    print(s.minDepth(root))
