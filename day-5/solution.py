class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        size = len(prices)
        profit = 0

        for today in range(size-1):
            stock = prices[today+1] - prices[today]
            if stock > 0:
               profit += stock 

        return profit


if __name__ == "__main__":
    sol = Solution()
    ans = sol.maxProfit([7,1,5,6,8,4])
    # ans = sol.maxProfit([1,2,3,4,5])
    # ans = sol.maxProfit([7,6,4,3,1])
    # ans = sol.maxProfit([6,1,3,2,4,7])
    # ans = sol.maxProfit([7,1,5,3,6,4])
    # ans = sol.maxProfit([2,1,4])    
    
    print (ans)
