n = 1000000
integers = []
integers.append(False)
integers.append(False)
i = 2
while i < n + 1:
    integers.append(True)
    i += 1
p = 2
while p * p <= n:
    if integers[p]:
        for i in range(p * 2, n + 1, p):
            integers[i] = False
    p = p + 1
primes = []
for p in range(2, n + 1):
    if integers[p]:
        primes.append(p)
print(primes)
