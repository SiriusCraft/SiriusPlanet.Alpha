class Solution(object):
    def isSubsequence(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if not len(s):
            return True
        if not len(t):
            return False
        for char in t:
            if not len(s):
                return True
            if char == s[0]:
                s = s[1:]
        return not len(s)
