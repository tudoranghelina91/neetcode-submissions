"""
Keep track of minimum buy-in
We store the max between the profit and difference between current price and min value
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        profit = 0
        n = len(prices)
        
        while r < n:
            if prices[l] >= prices[r]:
                l = r
            profit = max(profit, prices[r] - prices[l])

            r += 1

        return profit