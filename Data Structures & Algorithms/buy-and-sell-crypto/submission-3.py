"""
Keep track of minimum buy-in
We store the max between the profit and difference between current price and min value
"""
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minprice = prices[0]
        maxprofit = 0

        for price in prices:
            maxprofit = max(maxprofit, price - minprice)
            minprice = min(minprice, price)

        return maxprofit
