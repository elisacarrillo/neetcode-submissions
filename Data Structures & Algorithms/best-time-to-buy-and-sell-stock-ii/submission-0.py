class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        ptr1 = 0
        ptr2 = 1
        total_sub = 0
        while ptr2 < len(prices):
            sub = prices[ptr2] - prices[ptr1]
            if (sub > 0):
                total_sub += sub
            ptr1+=1
            ptr2+=1
            

            
        return total_sub


        