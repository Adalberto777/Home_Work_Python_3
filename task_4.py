# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> '101101'
# 3 -> '11'
# 2 -> '10'
# Примечание: Результат вернуть в виде строки. Не использовать функции преобразования типов: bin
def get_binar_num(num):
    binar = '' 
    while num > 0:
        binar = str(num % 2) + binar
        num = num // 2
    return binar


dec_num = int(input("Enter N: "))
 
print(get_binar_num(dec_num))
