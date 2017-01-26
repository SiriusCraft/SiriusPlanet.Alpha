class Solution(object):
    def findTheDifference(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        set_s = dict()
        set_t = dict()
        for char in s:
            if char in set_s:
                set_s[char] += 1
            else:
                set_s[char] = 1
        for char in t:
            if char in set_t:
                set_t[char] += 1
            else:
                set_t[char] = 1
        for char in set_t:
            if not char in set_s:
                return char
            if set_t[char] - set_s[char]:
                return char


if __name__ == '__main__':
    s = Solution()
    ans = s.findTheDifference("abcdea", "abcde")
    print(ans)
