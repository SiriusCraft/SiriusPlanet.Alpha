class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """
        nums_len = len(nums)
        i = 0
        max_range = 0
        while i < nums_len and i <= max_range:
            max_range = max(max_range, i+nums[i])
            i += 1
            print(max_range)
            if max_range+1 >= nums_len:
                return True
        return False

if __name__ == '__main__':
    s = Solution()
    print(s.canJump([0]))