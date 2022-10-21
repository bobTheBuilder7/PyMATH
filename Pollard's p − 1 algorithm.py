from math import gcd

n = 932723137786787759
B = 12
a = 2
primes = (2, 3, 5, 7)
output = 1
for i in primes:
    k = 1
    while True:
        if i ** k < B:
            k = k + 1
        else:
            output = output * (i ** (k - 1))
            break
b = a ** output % n

print(gcd(b - 1, n))
