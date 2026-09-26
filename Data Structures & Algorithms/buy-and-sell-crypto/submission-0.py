class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #we need to get the max profit 
        #we can use bruteforce but it would be O(n^2), but we need O(n)
        #so we use sliding window 
        #edge cases :
        #only one stock
        #no stock 
        #all are same prices 
        #highest price occurs before lowest 
        #duplicates 

        #because you can only buy today or later, not before, so sliding window is the best approach 

        #but at the lowest, and sell at highest 

        lowest = prices[0]
        max_profit = 0

        for i in range(1, len(prices)):
            if prices[i] < lowest: 
                lowest = prices[i]

            else: 
                profit = prices[i] - lowest 
                max_profit = max(max_profit, profit)

        return max_profit



