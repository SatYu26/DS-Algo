class Solution:
    def maxProfit(self, prices):
        # set day1 price as initial buy price
        buy_price = -prices[0]
        # set current max possible profit to 0
        max_profit = 0
        # set end of trade(eot) to the length of trading days
        eot = len(prices)
        
        for i in range(1, eot):
            # set aside current buy price
            current_buy_price = buy_price
            # if the succeeding day has lower price then swap with buy price
            buy_price = max(buy_price, max_profit - prices[i])
            # max profit should be max of previous max or current max
            max_profit = max(max_profit, current_buy_price + prices[i])
        return max_profit



class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        total = 0
        for i in range(len(prices)-1,0,-1):
            if prices[i]>prices[i-1]:
                total+=(prices[i]-prices[i-1])
            
        return total