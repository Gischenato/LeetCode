def maxProfit(prices: list[int]) -> int:
    buy = prices[0]

    total = 0
    for i in range(1, len(prices)):
        if prices[i] < prices[i-1]:
            total += prices[i-1] - buy
            buy = prices[i]

    total += prices[-1] - buy
    return total

print(maxProfit([7,1,5,3,6,4]))


def recursiv(index: int, buy: bool, prices: list[int]):
    if index == len(prices): return 0

    profit = 0

    if buy:
        chose_buy = -prices[index] + recursiv(index+1, False, prices)
        chose_skip = 0 + recursiv(index+1, True, prices)
        profit = max(chose_buy, chose_skip)
    else:
        chose_sell = prices[index] + recursiv(index+1, True, prices)
        chose_skip = 0 + recursiv(index+1, False, prices)
        profit = max(chose_sell, chose_skip)
    
    return profit

def recursiv_mem(index: int, buy: bool, prices: list[int], results: dict):
    if index == len(prices): return 0
    if (index, buy) in results: return results[(index, buy)]

    profit = 0

    if buy:
        chose_buy = -prices[index] + recursiv_mem(index+1, False, prices, results)
        chose_skip = 0 + recursiv_mem(index+1, True, prices, results)
        profit = max(chose_buy, chose_skip)
    else:
        chose_sell = prices[index] + recursiv_mem(index+1, True, prices, results)
        chose_skip = 0 + recursiv_mem(index+1, False, prices, results)
        profit = max(chose_sell, chose_skip)
    
    results[(index, buy)] = profit
    return profit



print(recursiv_mem(0,True,[1,2,3,4,5], {}))