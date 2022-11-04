"""Для заданных выборок вычислить их основные выборочные характеристики:
выборочное среднее, выборочную дисперсию, выборочный коэффициент асимметрии,
выборочный коэффициент эксцесса и построить гистограммы."""

import statistics
import pandas
import matplotlib.pyplot as plt
import numpy as np
import scipy.stats as stats

data = pandas.read_csv("data.csv")
x = [x for x in data['x'].tolist()]
y = [x for x in data['y'].tolist()]

# Выборочные характеристики X:

x_mean = statistics.mean(x)
print("Cреднее X: " + str(x_mean))

x_disp = np.var(x)
print("Дисперсия X: " + str(x_disp))

x_skew = stats.skew(x, bias=False)
print("Коэффициент асимметрии X: " + str(x_skew))

x_kurt = stats.kurtosis(x, bias=False)
print("Коэффициент эксцесса X: " + str(x_kurt))
print("--------------------------------------------")

# Выборочные характеристики Y:

y_mean = statistics.mean(y)
print("Cреднее Y: " + str(y_mean))

y_disp = np.var(y)
print("Дисперсия Y: " + str(y_disp))

y_skew = stats.skew(y, bias=False)
print("Коэффициент асимметрии Y: " + str(y_skew))

y_kurt = stats.kurtosis(y, bias=False)
print("Коэффициент эксцесса Y: " + str(y_kurt))

# Гистограмма
plt.hist(x, label='X')
plt.hist(y, label='Y')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.show()
