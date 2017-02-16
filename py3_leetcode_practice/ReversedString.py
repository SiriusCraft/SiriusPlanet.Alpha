"""
leetCode 344. Reverse String
use string build in method - join()
use list build in method - reversed()
split word with list()
"""
class Solution(object):
    def reverseString(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        reversed_l = reversed(l)
        return ''.join(reversed_l)