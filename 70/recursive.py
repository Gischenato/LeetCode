class Solution:
    results = {}

    def climbStairs(self, n: int) -> int:
        if n == 1: return 1
        if n == 2: return 2
        if n in self.results: return self.results[n]