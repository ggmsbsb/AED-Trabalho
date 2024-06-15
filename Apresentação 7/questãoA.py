import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados fornecidos
data = {
    'Ano': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Índice Gini': [0.496300241, 0.519534818, 0.586416119, 0.601124934, 0.542588302, 0.494670229, 0.526021771, 0.591726337, 0.597650597, 0.535307008]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Supondo que df['Ano'] e df['Índice Gini'] são listas de mesmo comprimento
ano = df['Ano']
indice_gini = df['Índice Gini']

# Calcular a média de 'Ano' e 'Índice Gini'
media_ano = sum(ano) / len(ano)
media_indice_gini = sum(indice_gini) / len(indice_gini)

# Calcular os valores necessários para o coeficiente angular e intercepto da reta de tendência linear
numerador = sum((x - media_ano) * (y - media_indice_gini) for x, y in zip(ano, indice_gini))
denominador = sum((x - media_ano) ** 2 for x in ano)

# Calcular o coeficiente angular (m) e o intercepto (b) da reta de tendência linear
m = numerador / denominador
b = media_indice_gini - m * media_ano

print("Fórmulas utilizadas para o coeficiente angular e intercepto da regressão linear: m = Σ[(xi - x_média) * (yi - y_média)] / Σ[(xi - x_média)^2], b = y_média - m * x_média")

# Prever o índice Gini para 2025
gini_previsto = m * 2025 + b

print("Fórmula utilizada para a previsão linear: y = m * x + b")

# Determinar se o país terá acesso à assistência internacional
assistencia_internacional = "terá acesso à assistência internacional" if gini_previsto > 0.6 else "NÃO terá acesso à assistência internacional"

# Resultados
print("\nDetalhes e Resultados:")
print(f"A equação de tendência linear é: y = {m}x + {b}")
print(f"O valor previsto para o ano de 2025 é igual a {gini_previsto:.6f}")
print(f"O país {assistencia_internacional}")

# Plotar os dados e a linha de tendência
plt.figure(figsize=(10, 6))
plt.scatter(ano, indice_gini, color='blue', label='Índice Gini Observado')
plt.plot(ano, [m * x + b for x in ano], color='red', label='Linha de Tendência Linear')
plt.xlabel('Ano')
plt.ylabel('Índice Gini')
plt.title('Tendência do Índice Gini')
plt.legend()
plt.grid(True)
plt.show()
