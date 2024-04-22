import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados fornecidos
anos = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
milho = np.array([330.4, 375.7, 196.3, 180.6, 223.1, 225.2, 243, 219.5, 203.5, 154.1, 153.2])
soja = np.array([186.7, 216, 147.32, 231, 246.68, 259.55, 241.6, 290.6, 292, 313.2, 318.5])
algodao = np.array([2015, 2357, 2319, 1577, 2576, 2835, 2700, 2853, 2851, 2537, 2883])

# Reshape dos dados para o formato aceito pelo scikit-learn
anos = anos.reshape(-1, 1)

# Modelo de regressão linear para milho
modelo_milho = LinearRegression()
modelo_milho.fit(anos, milho)
previsao_milho = modelo_milho.predict([[2024]])

# Modelo de regressão linear para soja
modelo_soja = LinearRegression()
modelo_soja.fit(anos, soja)
previsao_soja = modelo_soja.predict([[2024]])

# Modelo de regressão linear para algodão
modelo_algodao = LinearRegression()
modelo_algodao.fit(anos, algodao)
previsao_algodao = modelo_algodao.predict([[2024]])

# Média amostral e desvio padrão amostral para cada cultura
media_milho = np.mean(milho)
media_soja = np.mean(soja)
media_algodao = np.mean(algodao)

std_milho = np.std(milho, ddof=1)
std_soja = np.std(soja, ddof=1)
std_algodao = np.std(algodao, ddof=1)

# Tamanho da amostra
N = len(anos)

# Valor de z para um intervalo de confiança de 99%
z = 2.576  # Para um intervalo de confiança de 99%

# Calculando o valor de z usando a fórmula
# Formula dada na aula do dia 17. O valor de Z é dado pela diferença da média amostral e a média populacional dividido pela divisão do desvio padrão amostral pela raiz quadrada do tamanho da amostra.
z_milho = (media_milho - media_milho) / (std_milho / np.sqrt(N)) 
z_soja = (media_soja - media_soja) / (std_soja / np.sqrt(N))
z_algodao = (media_algodao - media_algodao) / (std_algodao / np.sqrt(N))

# Calculando o intervalo de confiança
intervalo_milho = z * (std_milho / np.sqrt(N))
intervalo_soja = z * (std_soja / np.sqrt(N))
intervalo_algodao = z * (std_algodao / np.sqrt(N))

# Imprimir previsões, limites superiores e limites inferiores
print(f"Previsão para a produção de milho em 2024: {previsao_milho[0]:.2f} mil toneladas")
print(f"Limite Inferior para milho: {previsao_milho[0]-intervalo_milho:.2f} mil toneladas")
print(f"Limite Superior para milho: {previsao_milho[0]+intervalo_milho:.2f} mil toneladas")

print("------------------------------------------------------------------------------------")

print(f"Previsão para a produção de soja em 2024: {previsao_soja[0]:.2f} mil toneladas")
print(f"Limite Inferior para soja: {previsao_soja[0]-intervalo_soja:.2f} mil toneladas")
print(f"Limite Superior para soja: {previsao_soja[0]+intervalo_soja:.2f} mil toneladas")

print("------------------------------------------------------------------------------------")

print(f"Previsão para a produção de algodão em 2024: {previsao_algodao[0]:.2f} mil toneladas")
print(f"Limite Inferior para algodão: {previsao_algodao[0]-intervalo_algodao:.2f} mil toneladas")
print(f"Limite Superior para algodão: {previsao_algodao[0]+intervalo_algodao:.2f} mil toneladas")
