# Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.

import random

n = random.randint(1, 100)
stop = 0
p = 2
print(n)
for i in range(n):
    if stop != 1:
        p = p ** i
        if p <= n:
            print(p, end=' ')
            p = 2
        else:
            stop = 1
    else:
        i = n