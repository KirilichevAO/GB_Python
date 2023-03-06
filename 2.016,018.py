# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению

import random

my_list = [random.randint(0, 100) for _ in range(10)]
number = int(input('Введите искомое число: '))
list_negativ = []
list_pozitiv = []
print(my_list)

if number not in my_list:
    for i in my_list:
        if number > i:
            list_negativ.append(i)
        elif number < i:
            list_pozitiv.append(i)
    print(max(list_negativ), min(list_pozitiv))
else:
    print(my_list.count(number))
