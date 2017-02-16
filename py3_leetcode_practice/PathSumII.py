# Definition for a binary tree node.
class TreeNode(object):
   def __init__(self, x):
      self.val = x
      self.left = None
      self.right = None

class Solution(object):
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """
        progress = []
        solution = []

        if root == None:
            return []

        def DFS(current, progress, current_sum):
            if is_goal(current, current_sum):
                progress.append(current)
                solution.append(progress[:])
                progress.remove(current)
                return
            if current in progress:
                return
            current_sum += current.val
            children = add_children(current)
            progress.append(current)
            for child in children:
                DFS(child, progress, current_sum)
            progress.remove(current)
            current_sum -= current.val

        def is_goal(current, current_sum):
            return current_sum+current.val == sum and current.left == None and current.right == None

        def add_children(current):
            children = set()
            if current.left:
                children.add(current.left)
            if current.right:
                children.add(current.right)
            return children
        DFS(root, progress, 0)

        solution_out = []
        for list in solution:
            p = []
            for i in range(len(list)):
                p.append(list[i].val)
            solution_out.append(p)
        return solution_out

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.left  = TreeNode(2)
    s = Solution()

    print(s.pathSum(root,3))
