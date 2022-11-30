from functools import lru_cache
import time
import sys
sys.setrecursionlimit(100000)
num = 1600

@lru_cache(maxsize = 256)
def fib_with_cache(n):
	if n < 2:
		return n
	return fib_with_cache(n-1) + fib_with_cache(n-2)
	
begin = time.time()
print(fib_with_cache(num))
end = time.time()

print("Time taken to execute the \
function with lru_cache is", end-begin)
