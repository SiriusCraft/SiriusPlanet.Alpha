# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        if not root:
            return []
        discovered = set()
        queue = []
        dic = []
        queue.append(root)
        root.count = 1
        while len(queue):
            current = queue[0]
            del queue[0]
            children = []
            if current.left:
                children.append(current.left)
            if current.right:
                children.append(current.right)
            for child in children:
                child.count = current.count+1
                if child not in discovered:
                    discovered.add(child)
                    queue.append(child)
                    dic.append((child.val, child.count))
        count_len = set()
        for (val, count) in dic:
            count_len.add(count)
        ans = [[] for _ in range(len(count_len)+1)]
        ans[len(count_len)].append(root.val)
        for val, count in dic:
            ans[len(count_len)-(count-1)].append(val)
        return ans

if __name__ == '__main__':
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.right = TreeNode(10)
    root.right.left = TreeNode(45)
    root.right.right = TreeNode(30)
    s = Solution()
    print(s.levelOrderBottom(root))