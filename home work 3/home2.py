# # 2-Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# # Пример:

# # [2, 3, 4, 5, 6] => [12, 15, 16];
# # [2, 3, 5, 6] => [12, 15]



import random

n = random.randint(1, 10)
print('\nРАНДОМНЫЙ СПИСОК ЧИСЕЛ ☻ ')
random_list = [random.randint(1, 99) for i in range(n)]

print(f'{random_list} \nКоличество чисел: {n}.')

print(f'Произведение пар первого и последнего числа:')

result_list = []
if len(random_list) % 2 == 0:
    for i in range(int(len(random_list) / 2)):
        result_list.append(random_list[i] * random_list[-(i + 1)])
        print(f'{random_list[i]} * {random_list[-(i + 1)]} = {result_list[i]}')
else:
     for i in range(int(len(random_list) / 2) + 1):
         result_list.append(random_list[i] * random_list[-(i + 1)])
         print(f'{random_list[i]} * {random_list[-(i + 1)]} = {result_list[i]}')

print(f'произведения чисел: {result_list}')




