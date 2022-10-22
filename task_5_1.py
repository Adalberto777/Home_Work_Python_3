# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]
def fibo(k):
    if k == 0:
        return 0
    elif k == 1 or k == 2:
        return 1
    else:    
        return fibo(k - 2) + fibo(k - 1)
    

n = int(input('Enter N: '))
 
nego_fibo_lst = []
for i in range(0, n + 1):
    nego_fibo_lst.append(fibo(i))
    nego_fibo_lst.insert(0, (((- 1) ** (i + 2)) * fibo(i+1)))

nego_fibo_lst.pop(0)

print(nego_fibo_lst)