def longestIncreasingPath(matrix: list[list[int]]) -> int:
    size_X = len(matrix[0])
    size_Y = len(matrix)

    mem = {}

    def is_valid(x,y):
        return x >= 0 and x < size_X and y >= 0 and y < size_Y
    
    def dfs(x,y):
        if (x,y) in mem: return mem[(x,y)]

        total = 1
        curr_value = matrix[y][x]
        paths = [1,]

        for X,Y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if not is_valid(X,Y): continue
            next_value = matrix[Y][X]
            if next_value > curr_value:
                paths.append(total + dfs(X,Y))

        total = max(paths)
            
        mem[(x,y)] = total
        return total

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            dfs(j,i)

    return max(mem.values())




print(longestIncreasingPath(
    # matrix=[[1]],
    # matrix=[[9,9,9],[9,9,9],[9,9,9]],
    # matrix=[[1]],
    # matrix=[[3,4,5],[3,2,6],[2,2,1]],
    # matrix=[[9,9,4],[6,6,8],[2,1,1]],
    matrix=[[1,4,5,8,9,12,13,16],[2,3,6,7,10,11,14,15]],
))
