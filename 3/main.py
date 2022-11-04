"""Для двух выборок из нормального распределения проверить гипотезу о равенстве средних
(одновыборочный критерий Стьюдента, все три альтернативы). """

import pandas
import scipy
import statistics

data = pandas.read_csv("data.csv")
x = [x for x in data['x'].tolist()]
y = [x for x in data['y'].tolist()]

alpha = 0.05

pm_x = statistics.mean(x)
stat_x, p_x = scipy.stats.ttest_1samp(x, popmean=pm_x)
print('Statistics=%.3f, p-value=%.3f' % (stat_x, p_x))
if p_x > alpha:
    print('Принять гипотезу для x')
else:
    print('Отклонить гипотезу для x')

print("----------------------------------------")

pm_y = statistics.mean(y)
stat_y, p_y = scipy.stats.ttest_1samp(y, popmean=pm_y)
print('Statistics=%.3f, p-value=%.3f' % (stat_y, p_y))
if p_y > alpha:
    print('Принять гипотезу для y')
else:
    print('Отклонить гипотезу для y')
