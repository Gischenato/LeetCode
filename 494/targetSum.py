def findTargetSumWays(nums: list[int], target: int) -> int:
        def rec(current, position, nums, target, mem):
            if position == len(nums): return 1 if current == target else 0
            if (current, position) in mem: return mem[(current, position)]
            total = 0
            total += rec(current + nums[position], position+1, nums, target, mem)
            total += rec(current - nums[position], position+1, nums, target, mem)
            
            mem[(current, position)] = total
            return mem[(current, position)]
        return rec(0, 0, nums, target, {})


print(findTargetSumWays([38,16,35,13,26,35,17,42,42,39,10,35,38,27,0,22,30,22,3,5], 11))