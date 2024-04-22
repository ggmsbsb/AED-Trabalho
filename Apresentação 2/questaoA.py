import numpy as np
import pandas as pd
import scipy.stats as stats

# Dados de produção das commodities agrícolas
dados_producao_agricola = {
    'Ano': [2013, 2014, 2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023],
    'Producao_Milho': [330.4, 375.7, 196.3, 180.6, 223.1, 225.2, 243, 219.5, 203.5, 154.1, 153.2],
    'Producao_Soja': [186.7, 216, 147.32, 231, 246.68, 259.55, 241.6, 290.6, 292, 313.2, 318.5],
    'Producao_Algodao': [2015, 2357, 2319, 1577, 2576, 2835, 2700, 2853, 2851, 2537, 2883]
}

df_producao_agricola = pd.DataFrame(dados_producao_agricola)

# Calculando a média móvel para suavizar os dados de produção
df_producao_agricola['Media_Movel_Milho'] = df_producao_agricola['Producao_Milho'].rolling(window=3).mean()
df_producao_agricola['Media_Movel_Soja'] = df_producao_agricola['Producao_Soja'].rolling(window=3).mean()
df_producao_agricola['Media_Movel_Algodao'] = df_producao_agricola['Producao_Algodao'].rolling(window=3).mean()

# Função para calcular os coeficientes de regressão linear
def calcular_coeficientes_regressao(x, y):
    n = len(x)
    soma_x = np.sum(x)
    soma_y = np.sum(y)
    soma_xy = np.sum(x * y)
    soma_x2 = np.sum(x**2)
    
    # Coeficientes da regressão linear
    A = (n * soma_xy - soma_x * soma_y) / (n * soma_x2 - soma_x**2)
    B = (soma_y - A * soma_x) / n
    
    return B, A

# Calculando os coeficientes de regressão para cada commodity
B_milho, A_milho = calcular_coeficientes_regressao(df_producao_agricola['Ano'], df_producao_agricola['Media_Movel_Milho'])
B_soja, A_soja = calcular_coeficientes_regressao(df_producao_agricola['Ano'], df_producao_agricola['Media_Movel_Soja'])
B_algodao, A_algodao = calcular_coeficientes_regressao(df_producao_agricola['Ano'], df_producao_agricola['Media_Movel_Algodao'])

# Previsão de produção para o ano de 2024
ano_previsao = 2024
previsao_producao_milho = B_milho + A_milho * ano_previsao
previsao_producao_soja = B_soja + A_soja * ano_previsao
previsao_producao_algodao = B_algodao + A_algodao * ano_previsao

# Imprimindo as previsões de produção para 2024
print(f'Previsão de produção de Milho para 2024: {previsao_producao_milho:.2f} milhares de toneladas')
print(f'Previsão de produção de Soja para 2024: {previsao_producao_soja:.2f} milhares de toneladas')
print(f'Previsão de produção de Algodão para 2024: {previsao_producao_algodao:.2f} milhares de toneladas')

# Calculando o intervalo de confiança de 99% usando Z-score
z_score = stats.norm.ppf(0.99)  # 99% de confiança (2,5% em cada cauda)
desvio_padrao_milho = df_producao_agricola['Media_Movel_Milho'].std()
desvio_padrao_soja = df_producao_agricola['Media_Movel_Soja'].std()
desvio_padrao_algodao = df_producao_agricola['Media_Movel_Algodao'].std()

# Calculando o intervalo de confiança para cada commodity
intervalo_confianca_milho = z_score * (desvio_padrao_milho / np.sqrt(len(df_producao_agricola)))
intervalo_confianca_soja = z_score * (desvio_padrao_soja / np.sqrt(len(df_producao_agricola)))
intervalo_confianca_algodao = z_score * (desvio_padrao_algodao / np.sqrt(len(df_producao_agricola)))

# Imprimindo os intervalos de confiança para as previsões
print(f'Intervalo de confiança para Milho: [{previsao_producao_milho - intervalo_confianca_milho:.2f}, {previsao_producao_milho + intervalo_confianca_milho:.2f}] milhares de toneladas')
print(f'Intervalo de confiança para Soja: [{previsao_producao_soja - intervalo_confianca_soja:.2f}, {previsao_producao_soja + intervalo_confianca_soja:.2f}] milhares de toneladas')
print(f'Intervalo de confiança para Algodão: [{previsao_producao_algodao - intervalo_confianca_algodao:.2f}, {previsao_producao_algodao + intervalo_confianca_algodao:.2f}] milhares de toneladas')
