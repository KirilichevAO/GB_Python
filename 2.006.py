# Вы пользуетесь общественным транспортом? Вероятно, вы расплачивались за проезд и получали билет с номером.
# Счастливым билетом называют такой билет с шестизначным номером, где сумма первых трех цифр равна сумме последних трех.
# Т.е. билет с номером 385916 – счастливый, т.к. 3+8+5=9+1+6.
# Вам требуется написать программу, которая проверяет счастливость билета.
#
# Пример:
# 385916 -> yes
# 123456 -> no

number = (input('Введите шестизначное число билета: '))
first_part = int(number[:3])
second_part = int(number[3:])

summa_first_part = first_part // 100 + first_part // 10 % 10 + first_part % 10
summa_second_part = second_part // 100 + second_part // 10 % 10 + second_part % 10

if summa_first_part == summa_second_part:
    print('yes')
else:
    print('no')