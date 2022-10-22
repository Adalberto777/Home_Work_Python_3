# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

positiv_fibo = [0, 1]
negative_fibo = [1, -1]
nego_fibo = []

n = int(input('Enter N: '))

for i in range(2, n + 1):
    positiv_fibo.append(positiv_fibo[i - 1] +  positiv_fibo[i - 2])
    negative_fibo.append(negative_fibo[i - 2] - negative_fibo[i - 1])

# for i in range(1, n):
#     nego_fibo.append(negative_fibo[n - i])

negative_fibo.reverse()
negative_fibo.pop(0)


print(negative_fibo + positiv_fibo)