def canJump(nums: list[int]) -> bool:
    total_jumps = nums[0]

    for i in range(1, len(nums)):
        if total_jumps == 0: return False

        total_jumps -= 1
        if nums[i] >= total_jumps: total_jumps = nums[i]

    return True

    


print(canJump([2,0,0]))