class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        for x in nums:
            if x == 0:
                nums.remove(x)
                nums.append(x)
        
