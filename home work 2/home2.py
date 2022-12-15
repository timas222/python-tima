# 2 - Напишите программу, которая принимает на вход число N и выдает набор произведений (набор - это список) чисел от 1 до N.
# Не используйте функцию math.factorial.

# Пример:
# - пусть N = 4, тогда [ 1, 2, 6, 24 ] #(1, 1*2, 1*2*3, 1*2*3*4)


number = int(input('Введите число: '))
my_list = []
for i in range(1, number + 1):
    my_list.append(round(((1 + 1/i)**i), 2))
print(my_list)
summ = 0
for i in range(len(my_list)):
    summ += my_list[i]
print(summ)