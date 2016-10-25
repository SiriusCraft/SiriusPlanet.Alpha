class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        ans = []
        dic = dict()
        for element in nums1:
            if element in dic:
                dic[element] += 1
            else:
                dic[element] = 1
        for element in nums2:
            if element in nums1:
                if dic[element] > 0:
                    ans.append(element)
                    dic[element] -= 1
        return ans

if __name__ == '__main__':
    nums1 = []
    nums2 = [1, 1, 1,2]
    s = Solution()
    s.intersect(nums1, nums2)
