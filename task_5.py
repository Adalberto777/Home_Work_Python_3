# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.
# Пример:
# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21]

def nega_fibo(n):
    str = []
    # str_temp = []
    str_nega_fibo = []
    if n == 0:
        str_nega_fibo = [0]        
    else:
        str = [0, 1]
        # str_temp = [0, 1]
        str_nega_fibo = [0, 1]
        a, b, j = 0, 1, - 1
        
        for i in range(2, n + 1):
            str.append(a + b)
            # str_temp.append((a + b) * j) 
            str_nega_fibo.append((a + b) * j) 
            a, b = b, a + b
            j *= -1              
        
        # for i in range(0, n):
        #     str_nega_fibo.append(str_temp[n - i])

        str_nega_fibo.pop(0)
        str_nega_fibo.reverse()        
        str_nega_fibo = str_nega_fibo + str
    return str_nega_fibo


n = int(input('Enter N: '))
    
print(nega_fibo(n))
