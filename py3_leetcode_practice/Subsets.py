"""
78. Subsets
There is difference between list.append() and list+another_list
append is destructive, but list+another_list is not, see line 20
I use list+another_list here
"""


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        nums_len = len(nums)
        sub_sets = [[]]
        for i in range(nums_len):
            temp_set = []
            for sub_set in sub_sets:
                temp_set.append(sub_set + [nums[i]])
            for _ in temp_set:
                sub_sets.append(_)
        return sub_sets


if __name__ == '__main__':
    s = Solution()
    print(s.subsets([1, 2]))
