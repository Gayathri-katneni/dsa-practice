class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        lowest = prices[0]
        maxProfit = 0
        for price in prices:
            if price < lowest:
                lowest = price
            profit= price-lowest
            if profit > maxProfit:
                maxProfit = profit
        return maxProfit
