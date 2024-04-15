def countBits(n: int):
    if n == 0: return 0
    if n == 1: return 1
    if n%2 == 0:
        return countBits(int(n/2))
    return countBits(int(n/2))+1

def countBits2(n):
    v = [0 for _ in range(n+1)]
    
    for i in range(len(v)):
        if i == 0: continue
        if i == 1: 
            v[i] = 1
            continue
        if i % 2 == 0:
            v[i] = v[int(i/2)]
        else:
            v[i] = v[int(i/2)] +1
    return v

# print(countBits(3))
print(countBits2(10))