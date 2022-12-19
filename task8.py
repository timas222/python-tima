# 1. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# # ['gfh5', 'gfh2', '67', 'jy32', '3put'] - ищем 32 - находим по индексу 3a




def input_l():
    data = input('введите значение в списке через пробел:\n').split('')
    return data
def find_val(data_l):
    what_find = input('когго ищем\n')
    result = []
    for i in range(len(data_l)):
        if what_find in data_l[i]:
            result.append(i)
    return result
elements = input_l()
result_l = find_val(elements)
print(f'Число присутстувует в списке по индексам:{result_l}')