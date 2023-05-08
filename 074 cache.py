import time
import functools

# nawet cache o rozmiarze 2 bardzo przyspiesza działanie
@functools.lru_cache(maxsize=5)
def fib(n):
    if n < 2:
        result = n
    else:
        result = fib(n-1) + fib(n-2)
    return result


start = time.time()

for i in range(31):
    result = fib(i)
    print('{0:2d} -> {1:8d}, time = {2:3.2f}s'.format(i, result, time.time() - start))

# statystyki hit/miss
print(fib.cache_info())
