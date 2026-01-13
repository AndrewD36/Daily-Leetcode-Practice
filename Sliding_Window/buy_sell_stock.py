class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        minPrice = prices[0]
        R = len(prices)
        profit = 0

        for i in range(0, len(prices)):
        
            if minPrice > prices[i]:
                minPrice = prices[i]

            if profit < prices[i] - minPrice:
                profit = prices[i] - minPrice

        return profit