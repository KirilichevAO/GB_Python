# Петя, Катя и Сережа делают из бумаги журавликов. Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно,
# что Петя и Сережа сделали одинаковое количество журавликов,
# а Катя сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#
# Пример:
# 6 -> 1  4  1
# 24 -> 4  16  4
# 60 -> 10  40  10

"""
total = int(input('Введите общее число журавликов: '))

Petya = total / 6
Katya = total / 6 * 4
Sereza = total / 6

print(f'{int(Petya)} {int(Katya)} {int(Sereza)}')
"""

# другой вариант решения
total = int(input('Введите общее число журавликов: ')) # 12

if total % 6 == 0:
    print(f'Петя и Сережа сделали по {int(total/6)}, а Катя {int(total * 2 / 3)}') # Петя и Сережа сделали по 2, а Катя 8
else:
    print('Кто то из детей крыса!')