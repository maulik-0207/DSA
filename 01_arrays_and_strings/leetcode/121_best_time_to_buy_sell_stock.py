# LeetCode 121 - Best Time to Buy and Sell Stock (Easy)
# Technique: Kadane's / Sliding Window
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/


class Solution:
    def maxProfit(self, prices):
        if not prices:
            return 0
        min_price = prices[0]
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            max_profit = max(max_profit, price - min_price)

        return max_profit
    
if __name__ == '__main__':
    sol = Solution()
    print(sol.maxProfit([7,1,5,3,6,4])) 
    print(sol.maxProfit([7,6,4,3,1]))
    
    
                
