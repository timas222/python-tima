# 3 - Дан массив размера N. После каждого отрицательного элемента массива вставьте элемент с нулевым значением.

# Пример:
# - пусть N = 4, тогда [28, -46, 14, -14] => [28, -46, 0, 14, -14, 0]


import random 
def creat_l(num):
    listnum = []
    for i in range(num):
        listnum.append(random.randint(-100, 100))
    return(listnum)
def put_zero_after_negative(list):
    for i in range(len(list)+1):
        if list[i] < 0:
            if i == len(list)-1:
                list.append(0)

            else:

                list.insert(i+1, 0)
    return list
n = input('Введите число:\n')
if n.isdigit():
    num = int(n)
    new_list = creat_l(num)
    print(f'исходный массив: {new_list}')
    try:
        print(f'массив с нулевым значением после каждого - элемента: {put_zero_after_negative}')
    except IndexError:
            print('все числа положительные')
else:
    print('вы ввели не число')
