"""Для двух выборок из нормального распределения проверить гипотезу о равенстве средних
(двухвыборочный критерий Стьюдента, все три альтернативы)."""

import pandas
import scipy

data = pandas.read_csv("data.csv")
x = [x for x in data['x'].tolist()]
y = [x for x in data['y'].tolist() if str(x) != 'nan']

alpha = 0.05

# для нормального распределения
stat, p = scipy.stats.ttest_ind(x, y)
print('Statistics=%.3f, p-value=%.3f' % (stat, p))
if p > alpha:
    print('Принять гипотезу')
else:
    print('Отклонить гипотезу')

print("----------------------------------------")

# среднее значение распределения, лежащего в основе первой выборки, меньше среднего значения распределения, лежащего в основе второй выборки
stat, p = scipy.stats.ttest_ind(x, y, alternative='less')
print('Statistics=%.3f, p-value=%.3f' % (stat, p))

if p > alpha:
    print('Принять гипотезу')
else:
    print('Отклонить гипотезу')

print("----------------------------------------")

# среднее значение распределения, лежащего в основе первой выборки, больше, чем среднее значение распределения, лежащего в основе второй выборки
stat, p = scipy.stats.ttest_ind(x, y, alternative='greater')
print('Statistics=%.3f, p-value=%.3f' % (stat, p))

if p > alpha:
    print('Принять гипотезу')
else:
    print('Отклонить гипотезу')
