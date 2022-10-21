from math import factorial, gcd
n = 932723137786787759
for _ in range(2, 100000):
    a = _
    x = False
    for i in range(1, 8):
        tak = pow(a, factorial(i)) - 1
        GCD = gcd(tak % n, n)
        if GCD != 1:
            x = True
            print(GCD)
            break
    if x:
        break
