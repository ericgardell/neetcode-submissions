class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # slopes ?
        buy = prices[0]
        buys = []
        profit = 0
        for i in range(1, len(prices)):
            sell = prices[i]
            profit = max([profit, sell - buy, 0])
            print(f"buy at {buy}, sell at {sell}, for ${profit}")
            if sell < buy:
                buy = prices[i]
        return profit
