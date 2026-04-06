class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1

        maxP = 0
        while b < len(prices) and s < len(prices) :
            if prices[b] >= prices[s]:
                b = s
                s += 1
            elif prices[b] < prices[s]:
                profit = prices[s] - prices[b]
                maxP = max(profit, maxP) 
                s+=1
        return maxP