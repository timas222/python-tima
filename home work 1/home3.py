# 3- Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


x = float(input('Пожалуйста введите x:'))
y = float(input('Пожалуйста введите y:'))
if x==0 or y==0:
    print("Пожалуйста введите корректные координаты!")
else:
    if x > 0 and y > 0:
         print('первая четверть')
    elif x < 0 and y > 0:
        print('вторая четверть')
    elif x < 0 and y < 0:
         print('третья четверть')
    elif x > 0 and y < 0:
         print('четвертая четверть')