"""
263 Ugly Number
"""
class Solution(object):
    def isUgly(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num<1:
            return False
        ugly_set = [2, 3, 5]
        for x in ugly_set:
            while num % x == 0:
                num /= x
        return num == 1

if __name__ == '__main__':
    s =Solution()
    print(s.isUgly(-1))