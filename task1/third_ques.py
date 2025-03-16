from funcs.csv_parser import parse_csv
from funcs.statistic import *


raw_list = parse_csv()

answer = {
    "Выборочное среднее": 0,
    "Выборочная дисперсия": 0,
    "Выборочная медиана": 0,
    "Межквартильный размах": 0
}

all_data = []
usa_data = []
not_usa_data = []

for raw in raw_list:
    integer = int(raw["Horsepower"])
    all_data.append(integer)

    if raw["Origin"] == "USA":
        usa_data.append(integer)
    else:
        not_usa_data.append(integer)


print("Для всех автомобилей:\n")
print("Выборочное среднее:", round(sample_mean(all_data), 2))
print("Выборочная дисперсия:", round(sample_variance(all_data), 2))
print("Выборочная медиана:", round(sample_median(all_data), 2))
print("Межквартильный размах (IQR):", round(interquartile_range(all_data), 2))
print("\n\n")

print("Для амерских автомобилей:\n")
print("Выборочное среднее:", round(sample_mean(usa_data), 2))
print("Выборочная дисперсия:", round(sample_variance(usa_data), 2))
print("Выборочная медиана:", round(sample_median(usa_data), 2))
print("Межквартильный размах (IQR):", round(interquartile_range(usa_data), 2))
print("\n\n")

print("Для НЕ амерских автомобилей:\n")
print("Выборочное среднее:", round(sample_mean(not_usa_data), 2))
print("Выборочная дисперсия:", round(sample_variance(not_usa_data), 2))
print("Выборочная медиана:", round(sample_median(not_usa_data), 2))
print("Межквартильный размах (IQR):", round(interquartile_range(not_usa_data), 2))
print("\n\n")
