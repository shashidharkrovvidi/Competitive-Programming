'''
https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

time complexity: O(n) where n is the size of the prices list
space complexity: O(1)
approach: when we sell on ith day, we must have bought on the day with minimum price from 1st to (i-1)th day to register a profit
we need to return the max running profit.
'''
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        min_price = prices[0] #we cannot sell on the 1st day, so initialize the price on the 1st day as the minimum price
        length = len(prices)
        max_profit = 0
        for i in range(1,length):
            min_price = min(min_price, prices[i-1]) #keeping track of the minimum stock price before the current day(i)
            max_profit = max(max_profit, prices[i] - min_price) #max_profit will be updated only when the current day's stock price is greater than the min_price
        return max_profit