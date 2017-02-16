"""
in this solution we implemented Boyer_Moore Majority Vote
Algorithm. Refer to:
https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
"""


class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return []
        candidate1, candidate2, count1, count2 = 0, 10, 0, 0
        for n in nums:
            if n == candidate1:
                count1 += 1
            elif n == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1 = n
                count1 = 0
            elif count2 == 0:
                candidate2 = n
                count2 = 0
            else:
                count1 -= 1
                count2 -= 1
        print(([n for n in (candidate1, candidate2) if nums.count(n) > len(nums) // 3]))
