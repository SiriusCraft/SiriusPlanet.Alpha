class Solution(object):
    def singleNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        dic = dict()
        ans = []
        for index in range(len(nums)):
            if nums[index] not in dic:
                dic[nums[index]] = 1
            else:
                dic[nums[index]] += 1
        for index in range(len(nums)):
            if dic[nums[index]] == 1:
                ans.append(nums[index])
        return ans