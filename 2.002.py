# Найдите сумму цифр трехзначного числа.
#
# Пример:
# 123 -> 6 (1 + 2 + 3)
# 100 -> 1 (1 + 0 + 0)

"""
number = int(input('Введите трехзначное число: ')) # 123
summa = 0

while number > 0:
    x = number % 10
    summa = summa + x
    number = number // 10
print(summa) # 6
"""

"""
# другой вариант решения задачи
number = int(input('Введите трехзначное число: ')) # 123
summa = number % 10 + number // 10 % 10 + number // 100
print(summa) # 6
"""

# другой вариант решения
number = '123'
summa = int(number[0]) + int(number[1]) + int(number[2])
print(summa) # 6
