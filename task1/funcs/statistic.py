import numpy as np


# Функция для вычисления выборочного среднего
def sample_mean(data):
    return sum(data) / len(data)


# Функция для вычисления выборочной дисперсии
def sample_variance(data):
    mean = sample_mean(data)
    return sum((x - mean) ** 2 for x in data) / (len(data) - 1)


# Функция для вычисления выборочной медианы
def sample_median(data):
    sorted_data = sorted(data)
    n = len(sorted_data)
    mid = n // 2
    if n % 2 == 0:
        return (sorted_data[mid - 1] + sorted_data[mid]) / 2
    else:
        return sorted_data[mid]


# Функция для вычисления межквартильного размаха (IQR)
def interquartile_range(data):
    sorted_data = sorted(data)
    q1 = np.percentile(sorted_data, 25)
    q3 = np.percentile(sorted_data, 75)
    return q3 - q1