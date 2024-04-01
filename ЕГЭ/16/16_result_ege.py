#задание № 16 
import functools as fn

@fn.lru_cache
def f(n):
    if n < 3: return n
    if n > 2: return (2*n-1)*(f(n-1)+f(n-2))
print(f(69)%(10**9+7))
