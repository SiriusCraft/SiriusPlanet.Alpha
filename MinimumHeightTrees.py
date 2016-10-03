"""
This class is a solution to leet_code 310:
----Minimum Height Trees---
I think there is some problem, when the graph is a
closed one, for example;
n = 4 , edges = [[0,1],[1,2],[2,3],[3,4]]
then BOOM
"""


class Solution(object):

    @staticmethod
    def findMinHeightTrees(n, edges):
        """
        This method is a solution to
        Minimum Height Trees
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        if n == 1:
            return [0]
        adj = [set() for i in range(n)]
        for [i, j] in edges:
            adj[i].add(j)
            adj[j].add(i)
        leaves = [i for i in range(n) if len(adj[i]) == 1]
        while n > 2:
            n -= len(leaves)
            new_leaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1:
                    new_leaves.append(j)
            leaves = new_leaves
        return leaves
