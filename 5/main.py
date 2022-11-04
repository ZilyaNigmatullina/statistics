"""Для двух выборок из нормального распределения проверить гипотезу о равенстве дисперсий
(критерий Фишера, все три альтернативы)."""

import pandas
import scipy.stats as st
import numpy as np

data = pandas.read_csv("data.csv")
x = [x for x in data['x'].tolist()]
y = [x for x in data['y'].tolist()]

alpha = 0.05


def f_test(a, b, alt="two_sided"):
    df1 = len(a) - 1
    df2 = len(b) - 1
    f = np.var(a) / np.var(b)
    if alt == "greater":
        p = 1.0 - st.f.cdf(f, df1, df2)
    elif alt == "less":
        p = st.f.cdf(f, df1, df2)
    else:
        p = 2.0 * (1.0 - st.f.cdf(f, df1, df2))
    return f, p


# 1
stat, p = f_test(x, y)
print('Statistics=%.3f, p-value=%.3f' % (stat, p))

if p > alpha:
    print('Принять гипотезу')
else:
    print('Отклонить гипотезу')

print("----------------------------------------")

# 2
stat, p = f_test(x, y, alt="less")
print('Statistics=%.3f, p-value=%.3f' % (stat, p))
if p > alpha:
    print('Принять гипотезу')
else:
    print('Отклонить гипотезу')

print("----------------------------------------")

# 3
stat, p = f_test(x, y, alt="greater")
print('Statistics=%.3f, p-value=%.3f' % (stat, p))
if p > alpha:
    print('Принять гипотезу')
else:
    print('Отклонить гипотезу')
