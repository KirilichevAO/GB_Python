# Написать программу, которая состоит 4 из этапов:
# - создает список из рандомных четырех значных чисел
# - принимает с консоли цифру и удаляет ее из всех элементов списка
# - цифры каждого элемента суммирует пока результат не станет однозначным числом
# - из финального списка убирает все дублирующиеся элементы
# - после каждого этапа выводить результат в консоль
# Пример:
# - 1 этап: [2634, 6934, 7286, 3353, 4602, 3176, 3796]
# - 2 этап: Введите цифру: 3
# - 2 этап: [264, 694, 7286, 5, 4602, 176, 796]
# - 3 этап: 264 -> 2+6+4 -> 12 -> 1+2 -> 3
# - 3 этап: [3, 1, 5, 5, 3, 5, 4]
# - 4 этап: [3, 1, 5, 4]

import random

list = [random.randint(1000, 9999) for _ in range(7)]
print(list)
list2 = []
list3 = []
number = input('Введите однозначное, положительное число: ')

for i in list:
    el = str(i)
    if number in el:
        el = el.replace(number, '')
    list2.append(el)
print(list2)

for i in list2:
    sum_num = sum([(int(el)) for el in i])
    while sum_num > 9:
        sum_num = sum([(int(el)) for el in str(sum_num)])
    list3.append(sum_num)
print(list3)
print(set(list3))
