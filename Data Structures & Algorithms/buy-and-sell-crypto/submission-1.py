class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit = l = r = 0
        while r < len(prices):
            if prices[l] > prices[r]:
                l = r
            else:
                maxprofit = max(maxprofit, prices[r] - prices[l])
                r += 1
        return maxprofit