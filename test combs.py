from math import exp, sqrt, e, log, isqrt, prod, gcd, ceil
from itertools import combinations
from reshetoEratosphena import resheto

n = 813967068547
print('колво символов', len(str(n)))
B = ceil(sqrt(exp(sqrt(log(n, e) * log(log(n, e), e)))))
print(B)
B = B * 3
suren = resheto(B)

def is_perfect_square(i: int) -> bool:
    return i == isqrt(i) ** 2
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


x = ceil(sqrt(n))
k = 0
combs = [1]
flag = False
slovar_vsego = {}
while True:
    perv = pow(x + k, 2)
    temp = perv - n
    if ez_prime_fact(temp) != {}:
        slovar_vsego[temp] = x + k
        for i in range(1, len(combs) + 1):
            for j in combinations(combs, i):
                j = list(j)
                j.append(temp)
                if is_perfect_square(prod(j)):
                    flag = True
                    break
            if flag:
                break
        if flag:
            break
        combs.append(temp)
    k = k + 1
if 1 in j:
    j.remove(1)
chisla1 = [slovar_vsego[i] for i in j]
chisla2 = isqrt(prod(j))
print(gcd((prod(chisla1) - chisla2), n))
print(gcd((prod(chisla1) + chisla2), n))