"""
dp[i+1] = max{dp[i], prices[i+1] - minprices}
minprices是区间[0,1,2...,i]内的最低价格
"""


class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        day_len = len(prices)
        if day_len < 2:
            return 0
        if prices[1] < prices[0] and day_len == 2:
            best = [0]
        else:
            best = [prices[1] - prices[0]]
        min_price = prices[0]
        for i in range(1, day_len):
            min_price = min(min_price, prices[i])
            best_now = max(best[i - 1], prices[i] - min_price)
            best.append(best_now)
        return best[-1]

    def maxProfit_outoftime(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if len(prices) == 0:
            return 0
        best_by_day = []
        for i in range(len(prices)):
            diff = 0
            for j in range(i + 1, len(prices)):
                if prices[j] - prices[i] >= diff:
                    diff = prices[j] - prices[i]
            best_by_day.append(diff)
        best = sorted(best_by_day)[len(best_by_day) - 1]

        print(best_by_day)
        print(best)


if __name__ == '__main__':
    s = Solution()
    print(s.maxProfit([2, 1]))
