def getRow(rowIndex: int) -> list[list[int]]:
    v = [1]
    for i in range(0, rowIndex):
        k = i+2
        new_v = [1 for _ in range(k)]

        for j in range(1, k-1):
            new_v[j] = v[j-1] + v[j]

        v = new_v
    return v


for i in range(10):
    print(i, getRow(i))