"""
Keep track of minimum buy-in
We store the max between the profit and difference between current price and min value
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = prices[0]
        profit = 0

        for p in prices:
            profit = max(profit, p - minimum)
            minimum = min(minimum, p)

        return profit
