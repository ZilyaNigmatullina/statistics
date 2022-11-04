"""Для заданной выборки из нормального распределения построить доверительные интервалы
для среднего и дисперсии, если обе они неизвестны."""

import pandas
import scipy
import statistics
import numpy

data = pandas.read_csv("data.csv")
x = [x for x in data['x'].tolist()]
y = [x for x in data['y'].tolist()]

alpha = 0.05

# доверительный интервал для среднего
interval = scipy.stats.norm.interval(confidence=alpha, loc=statistics.mean(x), scale=numpy.std(x))
print(interval)
