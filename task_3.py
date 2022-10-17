# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01, 12.00] => 0.19
# Примечание:
# Обратите внимание на элемент 5 и и 12.0. Они не участвуют в процессе т.к. дробная часть ноль.
# В списке могут быть как числа float, так и числа int.
# Посмотрите на методы числа float, возможно пригодятся.

def differens_max_min(str_modificate):
    max_fractional_part = str_modificate[0] - int(str_modificate[0])
    min_fractional_part = str_modificate[0] - int(str_modificate[0])

    for i in range(1, len(str_modificate)-1):
        if max_fractional_part < str[i] - int(str[i]):
            max_fractional_part = str_modificate[i] - int(str_modificate[i])

        if min_fractional_part > str_modificate[i] - int(str_modificate[i]):
            min_fractional_part = str_modificate[i] - int(str_modificate[i])

    result = max_fractional_part - min_fractional_part
    return result


def modificate_str(str):
    str_mod= []
    for i in range(len(str)):
        if str[i] - int(str[i]) != 0:
            str_mod.append((str[i]))
    return str_mod


str = [1.1, 1.2, 3.1, 5, 10.01, 12.00]
str_modificate = modificate_str(str)

print(differens_max_min(str))
print(f'{str} => {differens_max_min(str):.1f}') 