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

for row in m:
    print(row)

for i in m:
    for j in i:
        
