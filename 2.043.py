# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.
# Вводится список чисел. Все числа списка находятся на разных строках.

# import random # решение через словарь
#
# my_list = [random.randint(0, 10) for _ in range(int(input('Введите длинну списка: ')))]
# my_dict = {}

# for i in my_list:
#     my_dict[i] = my_dict.get(i, my_list.count(i) // 2)
# print(my_list)
# print(sum(my_dict.values()))

import random # решение через список

my_list = [random.randint(0, 10) for _ in range(int(input('Введите длинну списка: ')))]
count = 0

for i in my_list:
    if my_list.count(i) > 1:
        count += 1
print(my_list)
print(count // 2)

