class Solution0(object):
    """
    This solution causes O(n^2), which causes time limit excessed
    """

    def maxRotateFunction(self, A):
        """
        This method
        :type A: List[int]
        :rtype: int
        """
        if not len(A):
            return 0
        n = len(A)
        F = [0] * n
        A2 = A + A
        F = [0] * n
        for k in range(n):
            start = n - k
            for i in range(n):
                F[k] += i * A2[start + i]
        print(F)
        return sorted(F)[n - 1]


class Solution(object):
    def maxRotateFunction(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        if not len(A):
            return 0
        n = len(A)
        F = [0] * n
        sum_A = sum(A)
        for index, values in enumerate(A):
            F[0] += index * values
        ans = F[0]
        for i in range(n - 1):
            k = i + 1
            delta = n * A[n - k] - sum_A
            F[k] = F[k - 1] - delta
            ans = max(F[k], ans)
        return ans


if __name__ == '__main__':
    pass
