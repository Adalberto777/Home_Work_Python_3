# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.
# Пример:    
# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

users_nums = [2, 3, 5, 9, 3]

print(f'Sum => {sum(users_nums[1::2])}')

# from random import randint

# my_list = [randint(10, 100) for i in range(randint(5, 10))]
# print(my_list)
# sum_digit = 0

# for el in range(1, len(my_list), 2):
# sum_digit += my_list[el]