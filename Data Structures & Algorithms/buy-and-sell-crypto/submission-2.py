class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # brute force solution 

        profit = 0
        n = len(prices)
        
        for i in range(n-1):
            buy = prices[i]
            for j in range(i+1, n):
                sell = prices[j]
                profit = max(profit , sell - buy)
        return profit