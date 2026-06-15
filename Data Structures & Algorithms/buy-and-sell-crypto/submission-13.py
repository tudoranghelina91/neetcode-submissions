"""
Keep track of minimum buy-in
We store the max between the profit and difference between current price and min value
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        l, r = 0, 1
        maxprofit = 0
        n = len(prices)

        for r in range(n):
            if prices[r] <= prices[l]:
                l = r

            maxprofit = max(maxprofit, prices[r] - prices[l])

        return maxprofit