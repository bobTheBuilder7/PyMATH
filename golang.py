from math import ceil, sqrt, floor, gcd
from time import perf_counter
def is_square(n):
    l = sqrt(n)
    return (l - int(l)) == 0

def OLF(n):
    for ni in range(n, n * n, n):
        cs = ceil(sqrt(ni))
        pcs = pow(cs, 2, n)
        if is_square(pcs):
            return gcd(n, floor(cs - sqrt(pcs)))

print(OLF(27567710106515717570863))
print(perf_counter())