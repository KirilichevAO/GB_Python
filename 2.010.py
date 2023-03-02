# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

"""
import random

coins = int(input('Введите количество монет: ')) # 10
eagle = 0
tails = 0

for i in range(coins):
    sides = random.randint(0, 1)
    print(sides, end=', ') # 1, 0, 1, 0, 1, 0, 0, 1, 1, 0, 

    if sides == 0:
        eagle += 1
    elif sides > 0:
        tails += 1

if eagle > tails:
    print('\n', tails) # 5
else:
    print('\n', eagle)
"""


# другой вариант решения
n = int(input('Введите число монет: '))
count_zero = 0
count_one = 0

for i in range(n):
    x = int(input('Обозначте сторону монеты 0 или 1: '))
    if x == 0:
        count_zero += 1
    else:
        count_one += 1
if count_one > count_zero:
    print(f'0 => {count_zero}')
else:
    print(f'0 => {count_one}')
