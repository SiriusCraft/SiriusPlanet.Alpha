"""
This solution based on n must be
the mid when n's number more than
half length of a nums
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        return sorted(nums)[len(nums) / 2]
