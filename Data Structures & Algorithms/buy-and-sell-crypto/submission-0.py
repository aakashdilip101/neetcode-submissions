class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        i = 1
        cheapest_buy = prices[0]
        greatest_profit = 0

        while i < len(prices):
            if prices[i] - cheapest_buy > greatest_profit:
                greatest_profit = prices[i] - cheapest_buy
            
            if prices[i] < cheapest_buy:
                cheapest_buy = prices[i]
            
            i += 1
        
        return greatest_profit