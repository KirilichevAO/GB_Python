# Хакер Василий получил доступ к классному журналу и хочет заменить все свои минимальные оценки на максимальные.
# Напишите программу, которая заменяет оценки Василия, но наоборот: все максимальные – на минимальные.
import random

# Input: 5 -> 1 3 3 3 4
# Output: 1 3 3 3 1

estimates = [random.randint(1, 5) for i in range(10)]
print(estimates)
estimates_new = []

for i in estimates:
    max_estimates = max(estimates)
    min_estimates = min(estimates)
    if i == max_estimates:
        i = min_estimates
    estimates_new.append(i)
print(estimates_new)
