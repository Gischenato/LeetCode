def generate(numRows: int) -> list[list[int]]:
    v = [[1] for _ in range(numRows)]
    if numRows > 1: v[1] = [1,1] 
    for i in range(2, numRows):
        # print(i)
        new_v = [1 for _ in range(i+1)]
        # print(new_v)
        for j in range(1, i):
            new_v[j] = v[i-1][j-1] + v[i-1][j]

        v[i] = new_v


    return v
    
def print_list(l):
    for v in l:
        print(len(v)-1, v)

print_list(generate(15))