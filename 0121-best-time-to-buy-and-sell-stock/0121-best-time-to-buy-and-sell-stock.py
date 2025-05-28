class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        if(len(prices)==0):
            return 0
        else:
            minbuy=prices[0]
            profit=0
            for i in range(len(prices)):
                profit=max((prices[i]-minbuy),profit)
                minbuy=min(minbuy,prices[i])
            return profit