# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть,
# чтобы все монетки были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

import random

coins = int(input('Введите количество монет: '))
eagle = 0
tails = 0

for i in range(coins):
    sides = random.randint(0, 1)
    print(sides, end=', ')

    if sides == 0:
        eagle += 1
    elif sides > 0:
        tails += 1

if eagle > tails:
    print('\n', tails)
else:
    print('\n', eagle)
