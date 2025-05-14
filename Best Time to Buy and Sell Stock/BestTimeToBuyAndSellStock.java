/**
time complexity: O(n) where n is the size of the prices array
space complexity: O(1)
approach: to register a maximum profit, we need to sell a stock on the ith day. we must also have purhcased the stock on the day between 1st day and (i-1)th day when its price was minimum*/
class Solution {
    public int maxProfit(int[] prices) {
        int minPrice = prices[0]; // we cannot sell stock on the 1st day, initializing minPrice to prices[0]
        int maxProfit = 0;
        int len = prices.length;
        for(int i=1;i<len;i++)
        {
            minPrice = Math.min(minPrice,prices[i-1]);
            int currPrice = prices[i];
            maxProfit = Math.max(maxProfit,currPrice-minPrice); // maxProfit will be updated only when the current day's stock price is greater than the minPrice
        }
        return maxProfit;
    }
}