"""Для двух выборок найти коэффициент корреляции и построить линию регрессии.
Проверить значимость параметров регрессии."""

import pandas
from scipy import stats
import numpy as np
import matplotlib.pyplot as plt


def plot_regression_line(x, y, b):
    x = np.array(x)
    y = np.array(y)

    # plotting the actual points as scatter plot
    plt.scatter(x, y, color="m",
                marker="o", s=30)

    # predicted response vector
    y_pred = b[0] + b[1] * x

    # plotting the regression line
    plt.plot(x, y_pred, color="g")

    # putting labels
    plt.xlabel('x')
    plt.ylabel('y')

    # function to show plot
    plt.show()


def main():
    data = pandas.read_csv("data.csv")
    x = [x for x in data['x'].tolist()]
    y = [x for x in data['y'].tolist()]

    stat, p_value = stats.pearsonr(x, y)
    print("Коэффициент корреляции:", stat)
    linregress = stats.linregress(x, y)

    print("Коэффициенты регрессии:\nb_0 = {} \nb_1 = {}".format(linregress.intercept, linregress.slope))

    plot_regression_line(x, y, [linregress.intercept, linregress.slope])


if __name__ == "__main__":
    main()
