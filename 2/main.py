import pandas
from scipy.stats import chisquare

data = pandas.read_csv("data.csv")
x = [x for x in data['x'].tolist()]
y = [x for x in data['y'].tolist()]

# Вычисления для X
statisticX, pX = chisquare(x)
print("statisticX =", statisticX)
print("pX =", pX)

# Если значение p ≤ 0,05, то мы отклоняем нулевую гипотезу, т.e. предполагаем, что распределение не является нормальным.
# Если значение p > 0,05, то мы не можем отвергнуть нулевую гипотезу, т.е. предполагаем, что распределение является нормальным.

if pX > 0.05:
    print('Распределение X является нормальным')
else:
    print("Распределение X не является нормальным")

print("----------------------------------------")
# Вычисления для Y
statisticY, pY = chisquare(y)
print("statistic_Y =", statisticY)
print("p_Y =", pY)

if pY > 0.05:
    print('Распределение Y является нормальным')
else:
    print("Распределение Y не является нормальным")
