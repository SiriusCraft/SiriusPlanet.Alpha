"""
as for 'word', cannot be split with split() method.
then we use list() to make 'word' a list thus split 'word'
"""
class Solution(object):
    def isIsomorphic(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        list_s = list(s)
        list_t = list(t)
        if len(set(zip(list_s, list_t))) == len(set(list_s)) == len(set(list_t)) \
                and len(list_t) == len(list_s):
            return True
        else:
            return False
