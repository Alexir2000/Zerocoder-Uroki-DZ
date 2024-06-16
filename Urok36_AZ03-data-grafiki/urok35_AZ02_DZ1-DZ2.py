import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import time
import csv

mean = 0 # Среднее значение
std_dev = 1 # Стандартное отклонение
num_samples = 1000 # Количество образцов
data = np.random.normal(mean, std_dev, num_samples)

# for i in range(100):
#     print(data[i])

#
# Создаем гистограмму
plt.hist(data, bins=20)
plt.xlabel('значение')
plt.ylabel('Количество')
plt.title('Гистограмма ')
plt.grid(True)

# Показываем гистограмму
plt.show()

# ДЗ номер 2 Построй диаграмму рассеяния для двух наборов случайных данных
random_array1 = np.random.rand(5) # массив из 5 случайных чисел
random_array2 = np.random.rand(5)

print(random_array1)
print(random_array2)

plt.scatter(random_array1,random_array2)
plt.title("Диаграмма рассеивания")
plt.xlabel("набор 1")
plt.ylabel("Набор 2")
plt.show()


