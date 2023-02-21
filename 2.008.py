# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками (то есть разломить шоколадку на два прямоугольника).
#
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

n = int(input('Введите 1-ю сторону: '))
m = int(input('Введите 2-ю сторону: '))
k = int(input('Введите кол-во долек: '))

if k % n == 0 or k % m == 0:
    print('yes')
else:
    print('no')
