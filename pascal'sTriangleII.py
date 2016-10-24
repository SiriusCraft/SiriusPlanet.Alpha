class Solution(object):
    def getRow(self, rowIndex):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        rowIndex = rowIndex + 1
        if rowIndex == 1:
            row = [1]
        if rowIndex >= 2:
            row = [1, 1]
            for i in range(1, rowIndex - 1):
                for j in range(0, i):
                    a = row[0] + row[1]
                    row.append(a)
                    row.remove(row[0])
                row.append(1)
        return row

if __name__ == '__main__':
    s = Solution()
    print(s.getRow(0))
