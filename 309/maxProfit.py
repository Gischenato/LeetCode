from sys import setrecursionlimit
setrecursionlimit(2000)

def recursiv(index: int, buy: bool, prices: list[int], results:dict):
    if index >= len(prices): return 0

    if (index, buy) in results: return results[(index, buy)]

    profit = 0

    if buy:
        chose_buy = -prices[index] + recursiv(index+1, False, prices, results)
        chose_skip = 0 + recursiv(index+1, True, prices, results)
        profit = max(chose_buy, chose_skip)
    else:
        chose_sell = prices[index] + recursiv(index+2, True, prices, results)
        chose_skip = 0 + recursiv(index+1, False, prices, results)
        profit = max(chose_sell, chose_skip)
    
    results[(index, buy)] = profit
    return profit




prices = [1,2,3,0,2]
print(recursiv(0, True, prices, {}))