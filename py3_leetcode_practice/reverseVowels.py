"""
leetCode 345. Reverse Vowels of a String
similar to reversedString
"""
class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        l = list(s)
        vowel_set = {'a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U'}
        vowel_index_list = []
        vowel_char_list = []
        for i, c in enumerate(l):
            if c in vowel_set:
                vowel_index_list.append(i)
                vowel_char_list.append(c)
        for i in vowel_index_list:
            l[i] = vowel_char_list.pop()
        ans = ''.join(l)
        return ans
