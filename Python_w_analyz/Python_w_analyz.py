import matplotlib.pyplot as plt
import numpy as np
import pandas as ps

# загрузка данных из эксель файла
data_path = 'D:\path\Мск_5лет.xls'
data = ps.read_excel(data_path, skiprows = 6)
# перевод строки даты во внутренний формат даты
date = ps.to_datetime(data['Местное время в Москве (ВДНХ)'], dayfirst = True)
data['Дата'] = date
data = data.set_index('Дата')
#print(data.index)
# назначение дня отсчёта
first_day = ps.Timestamp(year = 2019, day = 1 , month = 1)
#print(first_day)
## ПОСТРОЕНИЕ ГРАФИКА
x = data.index
y = data['T']
data2 = data[data.index > first_day]
x2 = data2.index
y2 = data2['T']
plt.figure(figsize=(10, 5), num = 'График вариации температуры')  # размер графика + подпись
plt.xlabel('Дата') # подпись оси абсцисс
plt.ylabel('T температура') # подпись оси ординат
plt.subplot(211)
plt.plot(x, y, color='red', label='red line') # построение графика
plt.legend() # вывод легенды
plt.subplot(212)
plt.plot(x2, y2, color='blue', label='blue line')
plt.legend() # вывод легенды
plt.show() # вывод на экран
## ЗАПИСЬ В ЭКСЕЛЬ ФАЙЛ
data2.to_excel('D:\path\Test.xls')