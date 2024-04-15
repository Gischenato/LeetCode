def maxProfit(prices: list[int]) -> int:
    buy, sell = 0,1
    max_profit = 0

    while sell < len(prices):
        if prices[buy] < prices[sell]:
            max_profit = max(max_profit, prices[sell] - prices[buy])
        else:
            buy = sell
        sell +=1 
    return max_profit


print(maxProfit([7,4,1,2]))
