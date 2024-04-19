def numDistinct(self, s: str, t: str) -> int:
    mem = {}

    def solve(a: int, b: int) -> int:
        if b == len(t): return 1
        if a == len(s): return 0 

        if (a,b) in mem: return mem[(a,b)]

        
        if s[a] == t[b]:
            mem[(a,b)] = solve(a+1, b+1) + solve(a+1, b)
        else:
            mem[(a,b)] = solve(a+1, b)

        return mem[(a,b)]

    return solve(0,0)


print(numDistinct('a',
    s="babgbag",
    t="bag"
))
