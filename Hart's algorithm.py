from math import ceil, sqrt, gcd
from time import perf_counter
n = 932723137786787759
print('symbols amount', len(str(n)))
for i in range(1, n):
    s = ceil(sqrt(n * i))
    m = s ** 2 % n
    if ceil(sqrt(m)) ** 2 == m:
        t = sqrt(m)
        print(gcd(n, int(s-t)))
        break
print(perf_counter())