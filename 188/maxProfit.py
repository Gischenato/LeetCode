from sys import setrecursionlimit
setrecursionlimit(2000)

def recursiv(index: int, buy: bool, transactions:int, prices: list[int], max_transactions, results:dict):
    if index == len(prices) or transactions > max_transactions: return 0

    if (index, buy, transactions) in results: return results[(index, buy, transactions)]

    profit = 0

    if buy:
        chose_buy = -prices[index] + recursiv(index+1, False, transactions+1, prices, max_transactions, results)
        chose_skip = 0 + recursiv(index+1, True, transactions, prices, max_transactions, results)
        profit = max(chose_buy, chose_skip)
    else:
        chose_sell = prices[index] + recursiv(index+1, True, transactions, prices, max_transactions, results)
        chose_skip = 0 + recursiv(index+1, False, transactions, prices, max_transactions, results)
        profit = max(chose_sell, chose_skip)
    
    results[(index, buy, transactions)] = profit
    return profit



k = 2
prices = [2,4,1]
print(recursiv(0, True, 0, prices, k, {}))