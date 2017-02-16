class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        h = len(grid)
        w = len(grid[0]) if h else 0
        perimeter = 0
        for i in range(h):
            for j in range(w):
                if grid[i][j] == 1:
                    perimeter += 4
                else:
                    