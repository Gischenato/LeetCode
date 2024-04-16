def maxArea(height: list[int]) -> int:
    L, R = 0, len(height)-1

    best = 0

    while L < R:
        lenght = R-L
        smallest = min(height[L], height[R])
        curr_height = smallest * lenght
        if curr_height > best: best = curr_height
        # print(f'L({L})[{height[L]}]  R({R})[{height[R]}]   smallest: {smallest}')
        if height[L] == smallest: L+=1
        elif height[R] == smallest: R-=1

    return best
    



print(maxArea([1,8,6,2,5,4,8,3,7]))