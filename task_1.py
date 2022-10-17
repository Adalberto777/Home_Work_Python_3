# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:    
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

def sum_odd_index(str):
    sum_index = 0

    for i in range(1, len(str), 2):
        sum_index += str[i]
        
    return sum_index


str = [2, 3, 5, 9, 3, 7]

print(sum_odd_index(str))