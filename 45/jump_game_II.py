def canJump(nums: list[int]) -> bool:
    jumps = 0
    total_jumps = nums[0]

    for i in range(1, len(nums)):
        total_jumps -= 1
        if nums[i] >= total_jumps and i != len(nums)-1: 
            total_jumps = nums[i]
            jumps += 1

    return jumps

print(canJump([1,2]))