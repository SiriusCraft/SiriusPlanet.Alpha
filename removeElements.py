class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        while val in nums:
            for x in nums:
                print(x)
                if x == val:
                    nums.remove(x)
        return len(nums)
if __name__ == '__main__':
    s = Solution()
    print(s.removeElement([3,3,3],3))