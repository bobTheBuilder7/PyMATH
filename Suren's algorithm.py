from math import sqrt, ceil
from time import perf_counter
lol = False
n = 1027125644544889491233
sqr = ceil(sqrt(n))
listok = [1, 3, 7, 9]
# for i in listok:
#     for j in range(i, sqr, 10):
#         if n % j == 0 and j != 1:
#             print(j)
#             lol = True
#             break
#     if lol:
#         break

for j in range(2, sqr):
    if n % j == 0 and j != 1:
        print(j)
        print(n/j)
        break

print(perf_counter())