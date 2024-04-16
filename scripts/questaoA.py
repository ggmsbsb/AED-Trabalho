import numpy as np
import pandas as pd
import scipy.stats as stats

# Série histórica dos valores do ativo financeiro
serie = [
    {"dia": "1", "valor": 15.01},
    {"dia": "2", "valor": 18.92},
    {"dia": "3", "valor": 20.00},
    {"dia": "4", "valor": 15.78},
    {"dia": "5", "valor": 17.17},
    {"dia": "6", "valor": 16.23},
    {"dia": "7", "valor": 18.23},
    {"dia": "8", "valor": 18.00},
    {"dia": "9", "valor": 17.88},
    {"dia": "10", "valor": 19.02}
]

# Converter a série histórica para um DataFrame do pandas
df = pd.DataFrame(serie)
df['valor'] = df['valor'].astype(float)

# Calculando média móvel de 10 dias
media_10d = df['valor'].mean()

# Calculando média e desvio padrão da série histórica
media = df['valor'].mean()
desvio_padrao = df['valor'].std()

# Calculando intervalo de confiança bilateral de 95%
z_score = stats.norm.ppf(0.975)
intervalo_confianca = z_score * (desvio_padrao / np.sqrt(10))

# Determinando valores extremos para compra e venda de ações
valor_compra = media - intervalo_confianca
valor_venda = media + intervalo_confianca

# Calculando quantidade de ações adquiridas com base no capital inicial
quantidade_acoes = int(np.floor(1000000 / valor_compra))

# Calculando lucro previsto com base nos valores de compra e venda
lucro_previsto = quantidade_acoes * (valor_venda - valor_compra)

# Calculando lucro por ação
lucro_por_acao = lucro_previsto / quantidade_acoes

# Exibindo resultados
print(f"Valor ideal para compra: R${valor_compra:.2f}")
print(f"Valor ideal para venda: R${valor_venda:.2f}")
print(f"Quantidade de ações adquiridas: {quantidade_acoes}")
print(f"Lucro obtido previsto: R${lucro_previsto:.2f}")
print(f"Lucro por ação: R${lucro_por_acao:.2f}")
