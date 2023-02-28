# Дан список чисел. Определите, сколько в нем встречается различных чисел.
#
# Input: [1, 1, 2, 0, -1, 3, 4, 4]
# Output: 6

# import random
#
# my_list = [random.randint(0, 10) for _ in range(20)]
#
# print(my_list)
#
# new_list = []
#
# for item in my_list:
#     if item not in new_list:
#         new_list.append(item)
#
# print(new_list)
# print(len(new_list))

import random

my_list = [random.randint(0, 10) for _ in range(20)]

print(my_list)
print(len(set(my_list)))