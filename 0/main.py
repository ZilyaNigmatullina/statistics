import statistics
import pandas
import matplotlib.pyplot as plt
import numpy as np

# Количество мест в детских садах на 1000 детей дошкольного возраста. (за 2005-2016)
data = pandas.read_csv("Образование__доступность_дошкольного_образования.csv")
x = [x for x in data['value'].tolist() if str(x) != 'nan']

# Выборочное среднее
x_mean = statistics.mean(x)
print("Выборочное среднее: " + str(x_mean))

# Дисперсия
x_disp = np.var(x)
print("Дисперсия: " + str(x_disp))

# Медиана
x_med = statistics.median(x)
print("Медиана: " + str(x_med))

# Квантиль
q = np.quantile(x, 0.75)
print("Квантиль: " + str(q))

# Процентиль
p = np.percentile(x, 50)
print("Процентиль: " + str(p))

# Гистограмма
plt.hist(x)
plt.xlabel('x')
plt.ylabel('y')
plt.show()

# Ящик с усами
plt.boxplot(x)
plt.show()
