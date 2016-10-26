class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        day_len = len(prices)
        sum = 0
        if day_len < 2:
            return sum
        for i in range(1, day_len):
            if prices[i] > prices[i-1]:
                sum += prices[i]-prices[i-1]
        return sum


if __name__ == '__main__':
    s= Solution()
    print(s.maxProfit([1,2,4]))