from math import comb

def getRow(rowIndex: int) -> list[int]:
    pos = 0

    v = [0 for _ in range(rowIndex+1)]
    
    while pos != rowIndex+1:
        v[pos] = comb(rowIndex, pos)
        pos +=1
    return v

print(getRow(10))
