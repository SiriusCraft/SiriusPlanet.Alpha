"""
https://discuss.leetcode.com/topic/30421/share-my-thinking-process
"""


class Solution(object):
    def maxProfit1(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        day_num = len(prices)
        if day_num < 2:
            return 0
        sell = [0,0]
        buy = [-prices[0]]
        for date in range(1, day_num-1):
            buy.append(max(sell[date - 2] - prices[date], buy[date - 1]))
            sell.append(max(buy[date - 1] + prices[date], sell[date - 1]))
        # return sell[day_num]
        print("sell:\t{0}".format(sell))
        print("buy:\t{0}".format(buy))

    def maxProfit(self, prices):
        if len(prices) < 2:
            return 0
        sell, buy, prev_sell, prev_buy = 0, -prices[0], 0, 0
        buyy = []
        selll = []
        for price in prices:
            prev_buy = buy
            buyy.append(buy)
            buy = max(prev_sell - price, prev_buy)
            selll.append(sell)
            prev_sell = sell
            sell = max(prev_buy + price, prev_sell)
        return sell


if __name__ == '__main__':
    prices = [1, 2,3,0,2]
    print("prices:\t{0}".format(prices))
    s = Solution()
    s.maxProfit1(prices)
    s.maxProfit(prices)
