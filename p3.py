# Задача 3. В двумерном массиве хранятся средние дневные температуры с мая по сентябрь за прошлый год. 
# Каждому месяцу соответствует своя строка. 
# Определите самый жаркий и самый холодный 7-дневный промежуток этого периода. 
# Выведите его даты.
from random import randint as rdt

may = [rdt(12, 30) for _ in range(0, 31)]
june = [rdt(13, 36) for _ in range(0, 30)]
july = [rdt(16, 37) for _ in range(0, 31)]
august = [rdt(13, 33) for _ in range(0, 31)]
september = [rdt(4, 25) for _ in range(0, 30)]

m = [may, june, july, august, september]
month = { 1: 'Май', 2: 'Июнь', 3: 'Июль', 4: 'Август', 5: 'Сентябрь'}
max, min = m[0][0:7], m[0][1:8]

count = 1
for i in m:
    for j in range(0, len(i)):
        if sum(i[j:j + 7]) > sum(max) and len(i[j:j + 7]) > 6:
            max_start = j+1
            month_max = count
            max = i[j:j + 7]
        if sum(i[j:j + 7]) < sum(min) and len(i[j:j + 7]) > 6:
            min = i[j:j + 7]
            month_min = count
            min_start = j+1
    count += 1

def Result_week(s):
    result = []
    count = 0
    for _ in range(7):
        result.append(s + count)
        count += 1
    return tuple(result)

print("Средние дневные температуры с мая по сентябрь за прошлый год.")
cc = 1
for row in m:
    print(f'{month[cc]}: {row}')
    cc +=1
print(f'\nЖаркий месяц: {month[month_max]}\nСамый жаркий 7-дневный промежуток: {Result_week(max_start)}\nОбщая температура: {sum(max)} °C')
print(f'\nХолодный месяц: {month[month_min]}\nСамый холодный 7-дневный промежуток: { Result_week(min_start)}\nОбщая температура: {sum(min)} °C')

   