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
            return 0

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
                new_progress = []
                DFS(child, new_progress, 0)
            progress.remove(current)
            current_sum -= current.val

        def is_goal(current, current_sum):
            return current_sum+current.val == sum

        def add_children(current):
            children = set()
            if current.left:
                children.add(current.left)
            if current.right:
                children.add(current.right)
            return children
        DFS(root, progress, 0)
        if root.left:
            DFS(root.left,progress,0)
        if root.right:
            DFS(root.right,progress,0)
        solution_out = []

        for list in solution:
            p = []
            for i in range(len(list)):
                p.append(list[i].val)
            solution_out.append(p)
        return len(solution_out)

    def create_tree(self):
        list = [1, -2, -3, 1, 3, -2, None, -1]
        index = 1
        node = TreeNode(list[0])
        while index < len(list):
            self.create_tree(list[index], node.left)
            index +=1
            self.create_tree(list[index], node.right)
            index +=1

        return node

if __name__ == '__main__':
    root = TreeNode(1)
    root.right = TreeNode(1)
    root.left  = TreeNode(2)
    root.left.left = TreeNode(1)
    s = Solution()

    print(s.pathSum(root,1))
    n = s.create_tree()