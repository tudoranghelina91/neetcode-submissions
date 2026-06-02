"""
Keep track of minimum buy-in
We store the max between the profit and difference between current price and min value
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        n = len(prices)
        profit = 0

        while r < n:
            if prices[r] <= prices[l]:
                l = r

            profit = max(profit, prices[r] - prices[l])

            r += 1

        return profit