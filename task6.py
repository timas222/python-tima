# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.

# *Пример:*

# - Для N = 5: 1, -3, 9, -27, 81

list_random = []
numbers = int(input('введите число'))
for i in range(numbers):
    list_random.append((-3)**i)
print(list_random)