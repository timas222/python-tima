# 1 - Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. Учтите, что числа могут быть отрицательными

# Пример:

# 67.82 -> 23
# (-0.56) -> 11


num = input('Введите число: ')
def sum_digit(num):
    num = num.split('.')
    sum = 0
    for i in range(len(num)):
        digit = int(num[i])
        while digit != 0:
            sum += digit % 10
            digit = digit // 10
    return sum
print(f'Сумма {num} равна {sum_digit(num)}')