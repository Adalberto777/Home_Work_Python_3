## Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.
# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16];
# [2, 3, 5, 6] => [12, 15]

def product_pairs(str):
    list_num= []
    
    for i in range(0, int((len(str) + 1) / 2) ):
        
        list_num.append(str[i] * str[len(str) - 1 - i])
        
    return list_num


str = [2, 3, 4, 5, 6]

print(product_pairs(str))