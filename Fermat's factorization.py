from math import sqrt

n = 803293995722606153
print('symbols amount', len(str(n)))
x = round(sqrt(n)) - 1
k = 1
while True:
    temp = pow(x + k, 2) - n
    if temp >= 0:
        if sqrt(temp) == round(sqrt(temp)):
            x = x + k
            temp = sqrt(temp)
            break
    k = k + 1
print(x + temp, '*', x - temp)
# print((x + temp) * (x - temp))
