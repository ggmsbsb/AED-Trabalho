# Importando bibliotecas necessárias
import numpy as np
from sklearn.linear_model import LinearRegression

# Definindo os dados para os anos e a produção de milho, soja e algodão
anos = np.array([2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023])
milho = np.array([330.4, 375.7, 196.3, 180.6, 223.1, 225.2, 243, 219.5, 203.5, 154.1, 153.2])
soja = np.array([186.7, 216, 147.32, 231, 246.68, 259.55, 241.6, 290.6, 292, 313.2, 318.5])
algodao = np.array([2015, 2357, 2319, 1577, 2576, 2835, 2700, 2853, 2851, 2537, 2883])

# Moldando os dados dos anos para a forma correta
anos = anos.reshape(-1, 1)

# Criando modelos de regressão linear para cada cultura
modelo_milho = LinearRegression().fit(anos, milho) #Cria uma instancia de regressão linear usando os parametros de anos e milho.
modelo_soja = LinearRegression().fit(anos, soja)
modelo_algodao = LinearRegression().fit(anos, algodao)

# Fazendo previsões para o ano de 2024
previsao_milho = modelo_milho.predict([[2024]]) #Executa o modelo de regressão linear, Y = AX + B e formulas de A e B que não consigo colocar aqui por causa dos caracteres.
previsao_soja = modelo_soja.predict([[2024]])
previsao_algodao = modelo_algodao.predict([[2024]])

# Calculando média e desvio padrão amostral para cada cultura
media_milho, std_milho = np.mean(milho), np.std(milho, ddof=1)
media_soja, std_soja = np.mean(soja), np.std(soja, ddof=1)
media_algodao, std_algodao = np.mean(algodao), np.std(algodao, ddof=1)

# Obtendo tamanho da amostra
N = len(anos)

# Valor Z para um intervalo de confiança de 99%
z = 2.576

# Calculando intervalos de confiança para cada cultura
intervalo_milho = z * (std_milho / np.sqrt(N))
intervalo_soja = z * (std_soja / np.sqrt(N))
intervalo_algodao = z * (std_algodao / np.sqrt(N))

# Imprimindo previsões e intervalos de confiança para cada cultura
print(f"Previsão para a produção de milho em 2024: {previsao_milho[0]:.2f} mil toneladas")
print(f"Limite Inferior para milho: {previsao_milho[0]-intervalo_milho:.2f} mil toneladas")
print(f"Limite Superior para milho: {previsao_milho[0]+intervalo_milho:.2f} mil toneladas")

print(" ")
print("-------------------------------------------------------------------------------------")
print(" ")

print(f"Previsão para a produção de soja em 2024: {previsao_soja[0]:.2f} mil toneladas")
print(f"Limite Inferior para soja: {previsao_soja[0]-intervalo_soja:.2f} mil toneladas")
print(f"Limite Superior para soja: {previsao_soja[0]+intervalo_soja:.2f} mil toneladas")

print(" ")
print("-------------------------------------------------------------------------------------")
print(" ")

print(f"Previsão para a produção de algodão em 2024: {previsao_algodao[0]:.2f} mil toneladas")
print(f"Limite Inferior para algodão: {previsao_algodao[0]-intervalo_algodao:.2f} mil toneladas")
print(f"Limite Superior para algodão: {previsao_algodao[0]+intervalo_algodao:.2f} mil toneladas")

print(" ")
print("-------------------------------------------------------------------------------------")
print(" ")

#Valores de A, B e da equação de regressão linear. Só pra testar isso aq.
#print(f"Para Milho, A = {modelo_milho.coef_[0]:.2f}, B = {modelo_milho.intercept_:.2f}, formula é Y = {modelo_milho.coef_[0]:.2f}X + {modelo_milho.intercept_:.2f}")
#print(f"Para Soja, A = {modelo_soja.coef_[0]:.2f}, B = {modelo_soja.intercept_:.2f}, formula é Y = {modelo_soja.coef_[0]:.2f}X + {modelo_soja.intercept_:.2f}")
#print(f"Para Algodao, A = {modelo_algodao.coef_[0]:.2f}, B = {modelo_algodao.intercept_:.2f}, formula é Y = {modelo_algodao.coef_[0]:.2f}X + {modelo_algodao.intercept_:.2f}")