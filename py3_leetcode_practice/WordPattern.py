"""
use string.split() and zip() build-in method
"""


class Solution(object):
    def wordPattern(self, pattern, str):
        """
        :type pattern: str
        :type str: str
        :rtype: bool
        """
        list = str.split()
        if len(set(zip(pattern, list))) == len(set(pattern)) == len(set(list)) \
                and len(list) == len(pattern):
            return True
        else:
            return False