"""
Look at the ugly test case in __main__
"""


class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        len_s = len(s)
        ans = []
        if len_s < 10:
            return ans
        DNA_dic = dict()
        for start in range(len_s):
            sub_str = s[start:start + 10]
            if sub_str in DNA_dic:
                DNA_dic[sub_str] += 1
            else:
                DNA_dic[sub_str] = 1
        for sub_str in DNA_dic:
            if DNA_dic[sub_str] > 1:
                ans.append(sub_str)
        return ans


if __name__ == '__main__':
    s = "AAAAAAAAAAAAA"
    solu = Solution()
    solu.findRepeatedDnaSequences(s)
