from funcs.csv_parser import parse_csv
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns
from statsmodels.distributions.empirical_distribution import ECDF

raw_list = parse_csv()
result_dict = {}

all_list = []
sporty_list = []
large_list = []
van_list = []
small_list = []
midsize_list = []
compact_list = []

for raw in raw_list:
    power = raw["Horsepower"]
    type = raw["Type"]

    all_list.append(int(power))

    if type == "Small":
        small_list.append(int(power))
    elif type == "Sporty":
        sporty_list.append(int(power))
    elif type == "Compact":
        compact_list.append(int(power))
    elif type == "Midsize":
        midsize_list.append(int(power))
    elif type == "Van":
        van_list.append(int(power))
    elif type == "Large":
        large_list.append(int(power))


# Функция для расчета оптимального количества бинов
def optimal_bin_count(data):
    q75, q25 = np.percentile(data, [75, 25])  # Квартили
    iqr = q75 - q25  # Интерквартильный размах
    bin_width = 2 * iqr / (len(data) ** (1/3))  # Формула Фридмана-Дьякониса
    bin_count = max(1, int((max(data) - min(data)) / bin_width))  # Количество бинов
    return bin_count


# Эмпирическая функция распределения
ecdf = ECDF(van_list)
plt.figure(figsize=(8, 5))
plt.plot(ecdf.x, ecdf.y, marker=".", linestyle="none")
plt.xlabel("Horsepower")
plt.ylabel("Empirical CDF")
plt.grid()
plt.savefig("images/van/empirical_cdf.png")
plt.close()


# Вычисляем оптимальное количество бинов
bins = optimal_bin_count(van_list)
# Гистограмма
plt.figure(figsize=(8, 5))
plt.hist(van_list, bins=bins, edgecolor="black", alpha=0.7)
plt.xlabel("Horsepower")
plt.ylabel("Frequency")
plt.grid()
plt.savefig("images/van/histogram.png")
plt.close()

# Box-plot
plt.figure(figsize=(8, 5))
sns.boxplot(x=van_list)
plt.xlabel("Horsepower")
plt.grid()
plt.savefig("images/van/boxplot.png")
plt.close()
