# Заполните массив элементами арифметической прогрессии. Её первый элемент, разность и количество элементов нужно ввести с клавиатуры.
# Формула для получения n-го члена прогрессии: an = a1 + (n-1) * d.
# Каждое число вводится с новой строки.

# Ввод: 7 2 5
# Вывод: 7 9 11 13 15

# one_element = int(input('Введите значение первого элемента: '))
# difference = int(input('Введите разность: '))
# total_elements = int(input('Введите количество элементов: '))
# n_element = one_element + (total_elements - 1) * difference
# my_list = []
#
# for i in range(total_elements):
#     if one_element <= n_element:
#         my_list.append(one_element)
#         one_element += difference
# print(my_list)

one_element = int(input('Введите значение первого элемента: '))
difference = int(input('Введите разность: '))
total_elements = int(input('Введите количество элементов: '))

for i in range(total_elements):
    print(one_element + i * difference, end=' ')
