import collections

def numIslands(grid: list[list[str]]) -> int:
    MAX_X, MAX_Y = len(grid[0]), len(grid)
    
    def is_valid(x, y):
        return x >= 0 and x < MAX_X and y >= 0 and y < MAX_Y
    
    def dfs(x,y):
        print(x,y)
        if grid[y][x] == "0": return 0
        
        grid[y][x] = "0"

        for X,Y in [(x+1, y), (x-1, y), (x, y+1), (x, y-1)]:
            if is_valid(X,Y) and grid[Y][X] != "0":
                dfs(X,Y)

        return 1

    # total = 0 
    # for i in range(MAX_X):
    #     for j in range(MAX_Y):
    #         if grid[j][i] == '0': continue

    #         total += dfs(i, j)
    

    visited = set()

    def bfs(x,y):
        q = collections.deque()
        visited.add((x,y))
        q.append((x,y))

        while q:
            X, Y = q.popleft()
            
            for dX, dY in [(X+1, Y), (X-1, Y), (X, Y+1), (X, Y-1)]:
                if is_valid(dX, dY) and grid[dY][dX] == '1' and (dX, dY) not in visited:
                    q.append((dX, dY))
                    visited.add((dX, dY))
    


    total = 0
    for i in range(MAX_X):
        for j in range(MAX_Y):
            if grid[j][i] == '1' and (i,j) not in visited:
                bfs(i, j)
                total += 1

    return total




print(numIslands(
    grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","1"],
  ["0","0","1","0","1"]
]
))