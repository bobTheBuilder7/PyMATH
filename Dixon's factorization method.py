from math import exp, sqrt, e, log, floor, isqrt, prod, gcd
from random import randrange
from itertools import combinations

n = 89755
B = floor(sqrt(exp(sqrt(log(n, e) * log(log(n, e), e)))))
print(B)


def ez_prime_fact(n: int) -> dict:
    answer = {}
    flag = False
    while n != 1:
        for i in suren:
            if n % i == 0:
                answer[i] = answer.get(i, 0) + 1
                n = n / i
                flag = True
                break
        if not flag:
            return {}
        flag = False
    return answer


def is_perfect_square(i: int) -> bool:
    return i == isqrt(i) ** 2


suren = []
a_to_b = {}
sq = floor(sqrt(n))
while len(suren) < 100:
    b = (randrange(sq, n)) ** 2
    suren.append(b % n)
    a_to_b[b % n] = isqrt(b)

for i in combinations(suren, 2):
    if is_perfect_square(prod(i)):
        if i[0] != i[1]:
            mod1 = i[0] * i[0] % n
            mod2 = isqrt(prod(i)) % n
            if gcd(mod1 + mod2, n) != 1 and gcd(mod1 - mod2, n) != 1:
                print(gcd(mod1 + mod2, n))
                print(gcd(mod1 - mod2, n))
                break
