class Solution:
    results = {}

    def fib(self, n: int) -> int:
        if n <= 1: return n
        if n in self.results: return self.results[n]
        
        self.results[n] = self.fib(n-1) + self.fib(n-2)
        return self.results[n]
        