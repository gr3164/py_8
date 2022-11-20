# Задача 1. В каждой группе учится от 20 до 30 студентов.
# По итогам экзамена все оценки заносятся в таблицу.
# Каждой группе отведена своя строка. Определите группу с наилучшим средним баллом.
from random import randint
from statistics import mean

group = [[randint(2,5) for _ in range(0, randint(20, 30))] for _ in range(0, randint(2,11))]
gpa, group_number = mean(group[0]) , 1

def Compare_gpa(row, count):
    global gpa
    global group_number
    if mean(row) > gpa:
        gpa, group_number = mean(row), count
      
def Print_list(group):
    global gpa
    global group_number
    count = 1
    for row in group:
        Compare_gpa(row, count)
        print(f'{count}: {row}')
        count +=1    
    print(f'\nГруппа:  {group_number}\nСредний балл: {round(gpa, 2)}') 

Print_list(group)
