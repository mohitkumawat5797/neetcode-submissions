class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        # two pointer
        # prices = [10,1,5,6,7,1]

        l = 0
        r = 1
        profit = 0

        while r < len(prices):
            if prices[l] < prices[r]:
                buy = prices[r] - prices[l]
                profit = max(buy , profit)
            else :  # matlab if r < l then l will be buy date !!! 
                l = r
            r+=1
        return profit
        