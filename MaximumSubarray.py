"""
53. Maximum Subarray
DP: http://blog.csdn.net/linhuanmars/article/details/21314059
global best and local best
"""
class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nums_len = len(nums)
        if nums_len == 0:
            return 0
        local_best = nums[0]
        global_best = nums[0]
        for i in range(1,nums_len):
            local_best = max(local_best+nums[i],nums[i])
            global_best = max(local_best,global_best)
        return global_best

if __name__ == '__main__':
    s = Solution()
    s.maxSubArray([])