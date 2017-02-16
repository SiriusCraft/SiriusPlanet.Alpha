"""
那么怎样计算n!的质因子中所有5的个数呢？一个简单的方法是计算floor(n/5)。例如，
7!有一个5，10!有两个5。除此之外，还有一件事情要考虑。诸如25，125之类的数字有
不止一个5。例如，如果我们考虑28!，我们得到一个额外的5，并且0的总数变成了6。处
理这个问题也很简单，首先对n÷5，移除所有的单个5，然后÷25，移除额外的5，以此类推。
"""


class Solution(object):
    def trailingZeroes(self, n):
        """
        :type n: int
        :rtype: int
        """
        num_of_5 = 0
        x = 5
        while n >= x:
            num_of_5 += n / x
            x *= 5
        return int(num_of_5)


if __name__ == '__main__':
    n = 22
    s = Solution()
    print(s.trailingZeroes(n))
