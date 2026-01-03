class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        buy=prices[0]
        gain=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]
            elif prices[i]- buy >gain:
                gain=prices[i]-buy
        return gain
                