class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_val = float('inf')
        best_profit = 0

        for price in prices:
            best_profit = max(best_profit, price - min_val)
            min_val = min(min_val, price)
        return best_profit
        