import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os

# Создаем папку для сохранения изображений, если ее нет
output_dir = "plots"
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Истинные параметры логнормального распределения
mu0 = 4.91
sigma0_sq = 0.125
sigma0 = np.sqrt(sigma0_sq)

# Функция для оценки параметров методом моментов


def estimate_params(sample):
    x_bar = np.mean(sample)
    S2 = np.var(sample, ddof=1)
    hat_mu = np.log(x_bar) - 0.5 * np.log(1 + S2/(x_bar**2))
    hat_sigma_sq = np.log(1 + S2/(x_bar**2))
    return hat_mu, hat_sigma_sq


# Задаём размеры выборки и число повторений
sample_sizes = [20, 50, 100, 200, 500]
M = 1000

# Словари для хранения оценок
estimates_mu = {}
estimates_sigma_sq = {}

for n in sample_sizes:
    mu_estimates = []
    sigma_sq_estimates = []
    for _ in range(M):
        sample = np.random.lognormal(mean=mu0, sigma=sigma0, size=n)
        hat_mu, hat_sigma_sq = estimate_params(sample)
        mu_estimates.append(hat_mu)
        sigma_sq_estimates.append(hat_sigma_sq)
    estimates_mu[n] = np.array(mu_estimates)
    estimates_sigma_sq[n] = np.array(sigma_sq_estimates)

# --- Гистограммы для оценок μ ---
fig, axes = plt.subplots(1, len(sample_sizes), figsize=(20, 4), sharey=True)
for ax, n in zip(axes, sample_sizes):
    ax.hist(estimates_mu[n], bins=20, alpha=0.7, color='skyblue', edgecolor='black')
    ax.axvline(mu0, color='red', linestyle='--', label=r'$\mu_0$')
    ax.set_title(f"n = {n}")
    ax.set_xlabel(r'$\hat{\mu}$')
    ax.legend()
axes[0].set_ylabel("Частота")
plt.suptitle("Гистограмма оценок параметра $\mu$ (метод моментов)")
plt.tight_layout(rect=[0, 0, 1, 0.95])
hist_mu_path = os.path.join(output_dir, "hist_mu.png")
plt.savefig(hist_mu_path)
plt.show()

# --- Гистограммы для оценок σ² ---
fig, axes = plt.subplots(1, len(sample_sizes), figsize=(20, 4), sharey=True)
for ax, n in zip(axes, sample_sizes):
    ax.hist(estimates_sigma_sq[n], bins=20, alpha=0.7, color='lightgreen', edgecolor='black')
    ax.axvline(sigma0_sq, color='red', linestyle='--', label=r'$\sigma_0^2$')
    ax.set_title(f"n = {n}")
    ax.set_xlabel(r'$\hat{\sigma}^2$')
    ax.legend()
axes[0].set_ylabel("Частота")
plt.suptitle("Гистограмма оценок параметра $\sigma^2$ (метод моментов)")
plt.tight_layout(rect=[0, 0, 1, 0.95])
hist_sigma_path = os.path.join(output_dir, "hist_sigma.png")
plt.savefig(hist_sigma_path)
plt.show()

# --- Box-plot для оценок μ ---
plt.figure(figsize=(10, 6))
data_mu_box = [estimates_mu[n] for n in sample_sizes]
plt.boxplot(data_mu_box, labels=sample_sizes)
plt.axhline(mu0, color='red', linestyle='--', label=r'$\mu_0$')
plt.xlabel("Размер выборки n")
plt.ylabel(r"$\hat{\mu}$")
plt.title("Box-plot оценок параметра $\mu$")
plt.legend()
box_mu_path = os.path.join(output_dir, "box_mu.png")
plt.tight_layout()
plt.savefig(box_mu_path)
plt.show()

# --- Violin-plot для оценок μ ---
plt.figure(figsize=(10, 6))
plt.violinplot(data_mu_box, showmeans=True)
plt.xticks(range(1, len(sample_sizes) + 1), sample_sizes)
plt.axhline(mu0, color='red', linestyle='--', label=r'$\mu_0$')
plt.xlabel("Размер выборки n")
plt.ylabel(r"$\hat{\mu}$")
plt.title("Violin-plot оценок параметра $\mu$")
plt.legend()
violin_mu_path = os.path.join(output_dir, "violin_mu.png")
plt.tight_layout()
plt.savefig(violin_mu_path)
plt.show()

# --- Box-plot для оценок σ² ---
plt.figure(figsize=(10, 6))
data_sigma_box = [estimates_sigma_sq[n] for n in sample_sizes]
plt.boxplot(data_sigma_box, labels=sample_sizes)
plt.axhline(sigma0_sq, color='red', linestyle='--', label=r'$\sigma_0^2$')
plt.xlabel("Размер выборки n")
plt.ylabel(r"$\hat{\sigma}^2$")
plt.title("Box-plot оценок параметра $\sigma^2$")
plt.legend()
box_sigma_path = os.path.join(output_dir, "box_sigma.png")
plt.tight_layout()
plt.savefig(box_sigma_path)
plt.show()

# --- Violin-plot для оценок σ² ---
plt.figure(figsize=(10, 6))
plt.violinplot(data_sigma_box, showmeans=True)
plt.xticks(range(1, len(sample_sizes) + 1), sample_sizes)
plt.axhline(sigma0_sq, color='red', linestyle='--', label=r'$\sigma_0^2$')
plt.xlabel("Размер выборки n")
plt.ylabel(r"$\hat{\sigma}^2$")
plt.title("Violin-plot оценок параметра $\sigma^2$")
plt.legend()
violin_sigma_path = os.path.join(output_dir, "violin_sigma.png")
plt.tight_layout()
plt.savefig(violin_sigma_path)
plt.show()

# --- Вычисление статистик и формирование таблиц ---
data_mu_stats = []
data_sigma_stats = []

for n in sample_sizes:
    mu_hat = estimates_mu[n]
    bias_mu = np.mean(mu_hat) - mu0
    var_mu = np.var(mu_hat, ddof=1)
    mse_mu = var_mu + bias_mu**2
    data_mu_stats.append([n, bias_mu, var_mu, mse_mu])

    sigma_hat = estimates_sigma_sq[n]
    bias_sigma = np.mean(sigma_hat) - sigma0_sq
    var_sigma = np.var(sigma_hat, ddof=1)
    mse_sigma = var_sigma + bias_sigma**2
    data_sigma_stats.append([n, bias_sigma, var_sigma, mse_sigma])

df_mu = pd.DataFrame(data_mu_stats, columns=["n", "Bias(μ)", "Var(μ)", "MSE(μ)"])
df_sigma = pd.DataFrame(data_sigma_stats, columns=["n", "Bias(σ²)", "Var(σ²)", "MSE(σ²)"])

print("Результаты для оценок параметра μ:")
print(df_mu.to_string(index=False))
print("\nРезультаты для оценок параметра σ²:")
print(df_sigma.to_string(index=False))

# Сохраняем таблицы в CSV-файлы (при необходимости)
df_mu.to_csv(os.path.join(output_dir, "table_mu.csv"), index=False)
df_sigma.to_csv(os.path.join(output_dir, "table_sigma.csv"), index=False)
