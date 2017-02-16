class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        base = ord('A') - 1
        power = 1
        ans = 0
        for _ in range(len(s) - 1, -1, -1):
            ans += (ord(s[_]) - base) * power
            power *= 26
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.titleToNumber('AA'))
