"""
---371. Sum of Two Integers---
a = ~(a & MAX_INT) ^ MAX_INT
"""
class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        MOD = 0xffffffff
        MAX_INT = 0x7fffffff
        while b:
            c = a & b
            print(c)
            a = (a ^ b) & MOD
            b = c << 1 & MOD
        if a > MAX_INT:
            a = ~(a & MAX_INT) ^ MAX_INT
        return a
