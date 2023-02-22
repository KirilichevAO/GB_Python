# Дано натуральное число A > 1. Определите, каким по счету числом Фибоначчи оно является,
# то есть выведите такое число n, что φ(n)=A. Если А не является числом Фибоначчи, выведите число -1.
#
# Input: 5
# Output: 6

number = int(input('Введите натуральное число A > 1: '))
a = 0
b = 1
c = 0
count = 1

while c < number:
    c = a + b
    # a = b
    # b = c
    a, b = b, c # или
    count += 1
# if c == number:
#     print(count)
# else:
#     print(-1)
print(count if c == number else '- 1') # или

