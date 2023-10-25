import time
from functools import cache

@cache
def fibon(n):
    if n < 2:
        return n
    return fibon(n-1) + fibon(n-2)

start = time.time()
for i in range(100):
    print(i, fibon(i))
end = time.time()

print(end - start)