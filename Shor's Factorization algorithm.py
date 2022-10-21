from random import randint
from math import sqrt
while True:
    n = 1027125644544889491233
    lol = n
    b = randint(1, round(sqrt(n)) + 1)
    r = n % b
    while r:
        n, b = b, r
        r = n % b
    if b != 1:
        print(b, '*', lol/b)
        break

