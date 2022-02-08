def maxProfit(self, prices):
    mydict={}
    for i, a in enumerate(prices):
        mydict[a]=i
    prices.sort()
    for k in range(0, len(prices)):
        l,r=k,len(prices)-1
        while(l<r):
            buy=prices[l]
            sell=prices[r]
            if(mydict[sell] < mydict[buy]):
                r-=1
            else:
                return sell-buy
        l+=1
    return 0
print(maxProfit(maxProfit,[3,2,6,5,0,3]))

