# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону
# (т.е. не меньше заданного минимума и не больше заданного максимума)

# Ввод: [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# 5
# 15
# Вывод: [1, 9, 13, 14, 19]

# my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
# first_nomber = int(input('Введите значение начального диапазона: '))
# sekond_number = int(input('Введите значение конечного диапазона: '))
# my_list_index = []
#
# for i in my_list:
#     if i >= first_nomber and i <= sekond_number:
#         my_list_index.append(my_list.index(i))
# print(my_list_index)

my_list = [-5, 9, 0, 3, -1, -2, 1, 4, -2, 10, 2, 0, -9, 8, 10, -9, 0, -5, -5, 7]
first_nomber = int(input('Введите значение начального диапазона: '))
sekond_number = int(input('Введите значение конечного диапазона: '))
for i in range(len(my_list)):
    if first_nomber <= my_list[i] <= sekond_number:
        print(i, end=' ')
