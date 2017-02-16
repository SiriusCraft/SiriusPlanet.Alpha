"""
fuck leetcode that dose not support python3
fuck it!
http://www.cnblogs.com/grandyang/p/4741028.html
the answer actually circles by 9
"""
class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            c = 0
            while num:
                c += num % 10
                num /= 10
            num = c
        return num

        # while num > 9:
        #     sum = 0
        #     while num:
        #         sum += num % 10
        #         num = num / 10
        #         # print(sum)
        #     num = sum
        # return sum
        # print(sum)


if __name__ == '__main__':
    s = Solution()
    print(s.addDigits(10))
