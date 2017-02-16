class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            pascal = []
        if numRows == 1:
            pascal = [[1]]
        if numRows == 2:
            pascal = [[1], [1, 1]]
        if numRows > 2:
            pascal = [[] for _ in range(numRows)]
            pascal[0] = [1]
            pascal[1] = [1, 1]
            for i in range(1, numRows - 1):
                pascal[i + 1].append(1)
                temp = i
                for j in range(0, temp):
                    a = pascal[i][j] + pascal[i][j + 1]
                    pascal[i + 1].append(a)
                pascal[i + 1].append(1)
        return pascal
