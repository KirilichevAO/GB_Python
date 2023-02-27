# Петя и Катя – брат и сестра. Петя – студент, а Катя – школьница.
# Петя помогает Кате по математике. Он задумывает два натуральных числа X и Y (X,Y≤1000), а Катя должна их отгадать.
# Для этого Петя делает две подсказки. Он называет сумму этих чисел S и их произведение P.
# Помогите Кате отгадать задуманные Петей числа.

import random

x = random.randint(1, 1000)
y = random.randint(1, 1000)

s = x + y
p = x * y

x1 = int((s - ((-s) ** 2 - 4 * p) ** 0.5) / 2)
y1 = int((s + ((-s) ** 2 - 4 * p) ** 0.5) / 2)

print(s, p)
print(x1, y1)