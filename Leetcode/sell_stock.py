# def maxProfit(self, prices: list[int]):
#     maxprofit=0
#     for i in range(0, len(prices)-2):
#         for j in range(i+1, len(prices)-1):
#             if(prices[j]-prices[i]>maxprofit):
#                 maxprofit=prices[j]-prices[i]
#     return maxprofit
# print(maxProfit(maxProfit, [3,2,6,5,0,3]))

#approach2
#O(n) solution
def maxProfit(self, prices: list[int]):
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit
print(maxProfit(maxProfit,[7,1,5,3,6,4]))




        