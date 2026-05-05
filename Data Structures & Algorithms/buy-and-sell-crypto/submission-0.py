class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0
        sell = 1
        max_profit = 0
        for buy in range(len(prices)):
            for sell in range(len(prices)):
                profit = prices[sell] - prices[buy]
                if (profit > max_profit and sell > buy):
                    print("buy: " + str(buy) + " sell: " + str(sell))
                    max_profit = profit
                print( "BUY " + str(buy) + " SELL: " + str(sell))
                sell = sell + 1
            buy = buy + 1
            sell = buy + 1
        return max_profit
        