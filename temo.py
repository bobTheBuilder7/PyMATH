from math import isqrt, gcd

n = 3837523


def is_perfect_square(i: int) -> bool:
    return i == isqrt(i) ** 2


k = 1
numbers = []
while len(numbers) < 4:
    if n - k ** 2 > 0:
        if is_perfect_square(n - k ** 2):
            numbers.append(isqrt(n - k ** 2))
            numbers.append(k)
    else:
        print('не возможно для этого числа')
        exit()
    k = k + 1

a = numbers[0] - numbers[2]
b = numbers[0] + numbers[2]
c = numbers[3] - numbers[1]
d = numbers[3] + numbers[1]
m = gcd(a + c, d - b)
l = gcd(a - c, d + b)
print((gcd(a, c) / 2) ** 2 + (gcd(b, d) / 2) ** 2)
