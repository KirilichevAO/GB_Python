# Дана последовательность из N целых чисел и число K.
# Необходимо сдвинуть всю последовательность (сдвиг - циклический) на K элементов вправо, K – положительное число.
#
# Input: [1, 2, 3, 4, 5] k = 3
# Output: [4, 5, 1, 2, 3]

""""
import random

my_list = [random.randint(0, 20) for _ in range(10)]
k = int(random.randint(2, 7))

print(my_list)
print(k)
print(my_list[k:] + my_list[:k])
"""

""""
# другой вариант решения
shift = int(input('Введите сдвиг: '))
my_list = [i for i in range(10)]

print(my_list)

for i in range(shift):
    my_list.insert(0, my_list.pop(-1))

print(my_list)
"""

""""
# задача от Стоуна
import random

my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

my_dict = {}

for item in my_list:
    my_dict[item] = my_dict.get(item, 0) + 1
print(my_dict)

new_list = []

for key, value in my_dict.items():
    if value == 1:
        new_list.append(key)
print(new_list)
"""

# другой вариант решения
import random

my_list = [random.randint(0, 10) for _ in range(10)]
print(my_list)

new_list = []

for item in my_list:
    if my_list.count(item) == 1:
        new_list.append(item)
print(new_list)