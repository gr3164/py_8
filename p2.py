# Задача 2. Дана квадратная матрица, заполненная случайными числами. 
# Определите, сумма элементов каких строк превосходит сумму главной диагонали матрицы.
import random
import numpy as np

n = random.randint(2, 8)
m = np.random.randint(0, 10, size = (n, n))
number, a = 0, []

def Compare_sum(row, count):
    global m
    global number
    global a
    
    if sum(row) > sum(np.diagonal(m)):
        number = count
        a.append(number)
    
def Print(m):
    global a

    count = 1
    for row in m:
        Compare_sum(row, count)
        print(f'{count}: {row}')
        count += 1
    result = a if len(a) > 0 else 'Нет таких'
    print(f'\nСтроки(Сумма которых): {result} > Суммы главной диагонали({np.diagonal(m)}): {sum(np.diagonal(m))}')

Print(m)    
