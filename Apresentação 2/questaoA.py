import numpy as np
from sklearn.linear_model import LinearRegression

# Definindo os dados para os anos (X) e a produção de milho, soja e algodão (Y)
X = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
Y_milho = np.array([330.4, 375.7, 196.3, 180.6, 223.1, 225.2, 243, 219.5, 203.5, 154.1, 153.2])
Y_soja = np.array([186.7, 216, 147.32, 231, 246.68, 259.55, 241.6, 290.6, 292, 313.2, 318.5])
Y_algodao = np.array([2015, 2357, 2319, 1577, 2576, 2835, 2700, 2853, 2851, 2537, 2883])

# Moldando os dados dos anos (X) para a forma correta
X = X.reshape(-1, 1)

# Criando modelos de regressão linear para cada cultura
modelo_milho = LinearRegression().fit(X, Y_milho)
modelo_soja = LinearRegression().fit(X, Y_soja)
modelo_algodao = LinearRegression().fit(X, Y_algodao)

# Coeficientes da regressão linear (A e B)
A_milho, B_milho = modelo_milho.coef_[0], modelo_milho.intercept_
A_soja, B_soja = modelo_soja.coef_[0], modelo_soja.intercept_
A_algodao, B_algodao = modelo_algodao.coef_[0], modelo_algodao.intercept_

# Fazendo previsões para o ano de 2024
X_2024 = 2024
Y_2024_milho = A_milho * X_2024 + B_milho
Y_2024_soja = A_soja * X_2024 + B_soja
Y_2024_algodao = A_algodao * X_2024 + B_algodao

# Calculando média e desvio padrão amostral para cada cultura
media_milho, std_milho = np.mean(Y_milho), np.std(Y_milho, ddof=1)
media_soja, std_soja = np.mean(Y_soja), np.std(Y_soja, ddof=1)
media_algodao, std_algodao = np.mean(Y_algodao), np.std(Y_algodao, ddof=1)

# Obtendo tamanho da amostra
N = len(X)

# Valor Z para um intervalo de confiança de 99%
z = 2.576

# Calculando intervalos de confiança para cada cultura
intervalo_milho = z * (std_milho / np.sqrt(N))
intervalo_soja = z * (std_soja / np.sqrt(N))
intervalo_algodao = z * (std_algodao / np.sqrt(N))

# Imprimindo previsões e intervalos de confiança para cada cultura
print(f"Previsão para a produção de milho em 2024: {Y_2024_milho:.2f} mil toneladas")
print(f"Limite Inferior para milho: {Y_2024_milho-intervalo_milho:.2f} mil toneladas")
print(f"Limite Superior para milho: {Y_2024_milho+intervalo_milho:.2f} mil toneladas")

print(" ")
print("-------------------------------------------------------------------------------------")
print(" ")

print(f"Previsão para a produção de soja em 2024: {Y_2024_soja:.2f} mil toneladas")
print(f"Limite Inferior para soja: {Y_2024_soja-intervalo_soja:.2f} mil toneladas")
print(f"Limite Superior para soja: {Y_2024_soja+intervalo_soja:.2f} mil toneladas")

print(" ")
print("-------------------------------------------------------------------------------------")
print(" ")

print(f"Previsão para a produção de algodão em 2024: {Y_2024_algodao:.2f} mil toneladas")
print(f"Limite Inferior para algodão: {Y_2024_algodao-intervalo_algodao:.2f} mil toneladas")
print(f"Limite Superior para algodão: {Y_2024_algodao+intervalo_algodao:.2f} mil toneladas")

print(" ")
print("-------------------------------------------------------------------------------------")
print(" ")

# Exibindo todos os valores utilizados de forma detalhada
print("\nValores Utilizados nos Cálculos:")
print("Ano (X) | Produção de Milho (Y_milho) | Produção de Soja (Y_soja) | Produção de Algodão (Y_algodao)")
for i in range(len(X)):
    print(f"{X[i][0]} | {Y_milho[i]} | {Y_soja[i]} | {Y_algodao[i]}")
print(f"\nSoma dos valores:")
print(f"Soma de X: {np.sum(X):.2f}")
print(f"Soma de Y_milho: {np.sum(Y_milho):.2f}")
print(f"Soma de Y_soja: {np.sum(Y_soja):.2f}")
print(f"Soma de Y_algodao: {np.sum(Y_algodao):.2f}")
print(f"\nCoeficientes de Regressão Linear:")
print(f"A_milho: {A_milho:.2f}, B_milho: {B_milho:.2f}")
print(f"A_soja: {A_soja:.2f}, B_soja: {B_soja:.2f}")
print(f"A_algodao: {A_algodao:.2f}, B_algodao: {B_algodao:.2f}")
print(f"\nFórmulas de Regressão Linear (Y = A*X + B):")
print(f"Milho: Y = {A_milho:.2f}*X + {B_milho:.2f}")
print(f"Soja: Y = {A_soja:.2f}*X + {B_soja:.2f}")
print(f"Algodão: Y = {A_algodao:.2f}*X + {B_algodao:.2f}")
print(f"\nPrevisão para 2024 (X = 2024):")
print(f"Previsão milho: {Y_2024_milho:.2f}")
print(f"Previsão soja: {Y_2024_soja:.2f}")
print(f"Previsão algodão: {Y_2024_algodao:.2f}")
print(f"\nMédias:")
print(f"Média milho: {media_milho:.2f}")
print(f"Média soja: {media_soja:.2f}")
print(f"Média algodão: {media_algodao:.2f}")
print(f"\nDesvios Padrão:")
print(f"Desvio padrão milho: {std_milho:.2f}")
print(f"Desvio padrão soja: {std_soja:.2f}")
print(f"Desvio padrão algodão: {std_algodao:.2f}")
print(f"\nIntervalos de Confiança (99%):")
print(f"Intervalo milho: ±{intervalo_milho:.2f}")
print(f"Intervalo soja: ±{intervalo_soja:.2f}")
print(f"Intervalo algodão: ±{intervalo_algodao:.2f}")
