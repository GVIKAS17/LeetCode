class Solution(object):
    def maxProfit(self, prices):
        min = prices[0]
        maxp = 0
        for i in range(1,len(prices)):
            if (prices[i] < min):
                min = prices[i]
            else:
                maxp = max(maxp, prices[i] - min)
        return maxp