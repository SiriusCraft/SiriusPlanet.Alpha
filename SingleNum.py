class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for index in range(len(nums)-1):
            nums[index+1] = nums[index] ^ nums[index+1]
        print(nums[len(nums)-1])
        return nums[len(nums)-1]

# if __name__ == '__main__':
#     nums = [1,2,3,1,2]
#     s = Solution()
#     s.singleNumber(nums)