def canCompleteCircuit(gas: list[int], cost: list[int]) -> int:
    if sum(gas) < sum(cost): return -1

    diff = [g-c for g,c in zip(gas, cost)]

    total = 0
    res = 0

    for i in range(len(diff)):
        total += diff[i]
        if total < 0:
            total = 0
            res = i+1
    return res
    
print(canCompleteCircuit([1,2,3,4,5], [4,3,1,5,2]))