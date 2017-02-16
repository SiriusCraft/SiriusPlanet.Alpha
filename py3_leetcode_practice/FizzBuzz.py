class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        l = []
        for i in range(n):
            num = i + 1
            if (num % 3 == 0) and (num % 5 != 0):
                l.append("Fizz")
            elif (num % 3 != 0) and (num % 5 == 0):
                l.append("Buzz")
            elif (num % 15 == 0):
                l.append("FizzBuzz")
            else:
                l.append("{0}".format(num))
        return l


if __name__ == '__main__':
    s = Solution()
    s.fizzBuzz(16)
