# 3-Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# Пример:

# [1.1, 1.2, 3.1, 5.17, 10.02] => 0.18 или 18
# [4.07, 5.1, 8.2444, 6.98] - 0.91 или 91



from decimal import Decimal
import random

n = random.randint(6, 18)
random_list = [round(random.uniform(0, 3), random.randint(0, 3)) for i in range(n)]

print(random_list)
dec_list = []

for i in range(0, len(random_list)):
    if random_list[i] % 1 > 0:
        random_list[i] = (random_list[i])
        dec_list.append(round(random_list[i] % 1, 3))

if len(dec_list) == 1:
    print('В списке только один элемент с дробной частью.')
else:
    diff = round(max(dec_list) - min(dec_list), 3)
    print(f'Разница между максимальным {max(dec_list)} и минимальным {min(dec_list)}')
    print(f'значениями дробной части элементов равна: {diff}')