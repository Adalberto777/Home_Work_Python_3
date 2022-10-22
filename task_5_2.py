# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def nego_fibo(k):
    if k == 0: return 0
    if k == 1: return 1
    if k == - 1: return 1
    if k == 2: return 1
    if k == - 2: return - 1
    if k > 2: return nego_fibo(k - 2) + nego_fibo(k - 1)
    if k < - 2: return nego_fibo(k + 2) - nego_fibo(k + 1)

    

n = int(input('Enter N: '))

for i in range(- n, n + 1):
    print(nego_fibo(i), end=", ")