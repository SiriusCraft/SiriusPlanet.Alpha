"""
I thought it is really tricky.
Why does it works without condition n!=dic[target-nums[n]]
in Another_solution?????
It determines target-num[n] not in dict first
and then add num[n] into dict, which avoid
target - num[n] == num[n] problem
"""


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        dic = {nums[i]: i for i in range(len(nums))}
        for n in range(len(nums)):
            if target - nums[n] in dic and n != dic[target - nums[n]]:
                return [n, dic[target - nums[n]]]


class Another_Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        dict = {}
        for n in range(len(num)):
            x = num[n]
            if target - x in dict:
                return (dict[target - x], n)
            dict[x] = n
