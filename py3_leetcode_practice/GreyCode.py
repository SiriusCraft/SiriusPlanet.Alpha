class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        if n == 0:
            return [0]
        if n == 1:
            return [0, 1]
        current = [0, 1]
        power = 1
        for i in range(1, n):
            reversed_current = []
            current_len = len(current)
            power *= 2
            for j in range(current_len - 1, -1, -1):
                reversed_current.append(current[j]+power)
            current = current+reversed_current
        return current
        print(current)


if __name__ == '__main__':
    s = Solution()
    s.grayCode(3)
