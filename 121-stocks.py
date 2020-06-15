'''
Say you have an array for which the ith element is the price of a given stock on day i.
If you were only permitted to complete at most one transaction 
(i.e., buy one and sell one share of the stock), design an algorithm to find the maximum profit.
Note that you cannot sell a stock before you buy one.
'''
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        min_price = sys.maxsize
        max_profit = 0
        
        for i in prices:
            if i < min_price:
                min_price = i
            elif i-min_price>max_profit:
                max_profit = i-min_price
        
        return max_profit