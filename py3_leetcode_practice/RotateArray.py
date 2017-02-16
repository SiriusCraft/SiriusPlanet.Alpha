class Solution:
    # @param nums, a list of integer
    # @param k, num of steps
    # @return nothing, please modify the nums list in-place.
    def rotate(self, nums, k):
        n = len(nums)
        if k > 0 and n > 1:
            nums[:] = nums[n - k:] + nums[:n - k]


if __name__ == '__main__':
    s = Solution()
    s.rotate([1, 2], 1)
