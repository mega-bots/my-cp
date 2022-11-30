def isKthBitSet(n, k):
    return  n & (1 << (k - 1))
print(isKthBitSet(2,2))
