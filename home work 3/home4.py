# 4- Напишите программу, которая будет преобразовывать десятичное число в двоичное. Подумайте, как это можно решить с помощью рекурсии.
# Не использовать функцию bin

# Пример:

# 45 -> 101101
# 3 -> 11
# 2 -> 10


s = "-вот ваше двоично число"
n = int(input("Введите число для преобразовывания десятичного числа в двоичное:\n"))
while n != 0:
    s = str(n%2) + s
    n //=2
print(s)