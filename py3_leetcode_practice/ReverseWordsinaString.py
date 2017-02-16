class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        new = ''
        l = s.split()
        for i in range(len(l)-1, -1, -1):
            new += l[i]
            if i != 0:
                new += ' '
        return new
        print(new)


if __name__ == '__main__':
    s = Solution()
    s.reverseWords("this is no good")
