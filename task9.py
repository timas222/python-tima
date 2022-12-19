# 2. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# Пример:

# список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# список: [], ищем: "123", ответ: -1



def input_list():
    data = input('введите значение:\n'). split(' ')
    return data

def find_value(data_list):
    what_find = input('Кого ищем:\n')
    count = 0
    for i in range(len(data_list)):
        if what_find in data_list[i]:
            count += 1
            if count == 2:
                return f'индекс второго вхождения - {i}, а позиция - {i + 1}'
    else:
        return 'нет'
elements = input_list()
result = find_value(elements)
print(result)