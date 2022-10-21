from time import perf_counter

def resheto(n2: int) -> list:
    n1 = 2
    spisok = [2, 3, 5]

    for i in range(n1, n2 + 1):
        if i % 2 != 0 and i % 3 != 0 and i % 5 != 0:
            spisok.append(i)
    for number in spisok:
        if number ** 2 > n2:
            break
        flag = False
        for anothernumber in spisok:
            if anothernumber % number == 0 and flag == False:
                flag = True
            elif anothernumber % number == 0:
                spisok.remove(anothernumber)

    return spisok


start = perf_counter()
print(resheto(1000))
print(perf_counter()-start)