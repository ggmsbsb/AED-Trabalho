import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

# Dados de datas e cotações
data = ['01/08', '02/08', '03/08', '04/08', '05/08', '08/08', '09/08', '10/08', '11/08', '12/08', '15/08', '16/08', '17/08', '18/08', '19/08', '22/08', '23/08', '24/08', '25/08', '26/08', '29/08', '30/08', '31/08']
cotacao = [5.21, 5.26, 5.29, 5.29, 5.26, 5.23, 5.16, 5.09, 5.06, 5.02, 5.01, 5.00, 5.03, 5.08, 5.15, 5.21, 5.26, 5.31, 5.29, 5.27, 5.23, 5.18, 5.11]

# Criar DataFrame
df = pd.DataFrame({'Data': data, 'Cotação': cotacao})

# Convertendo a coluna Data para datetime
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m').dt.strftime('%d/%m')

# Adicionando uma coluna com os dias decorridos para facilitar a regressão linear
dias = np.arange(1, len(data) + 1)
df['Dias'] = dias

# Mostrar tabela de valores de X (Dias) e Y (Cotação)
print("-----------------------------")
print("1) Tabela de Dados:")
print(df.to_string(index=False))

# Calcular soma de X (Dias) e Y (Cotação)
soma_X = df['Dias'].sum()
soma_Y = df['Cotação'].sum()

# Calcular a média de 'Dias' e 'Cotação'
media_dias = soma_X / len(dias)
media_cotacao = soma_Y / len(cotacao)

# Calcular os valores necessários para o coeficiente angular e intercepto da reta de tendência linear
numerador = sum((x - media_dias) * (y - media_cotacao) for x, y in zip(dias, cotacao))
denominador = sum((x - media_dias) ** 2 for x in dias)

# Calcular o coeficiente angular (m) e o intercepto (b) da reta de tendência linear
m = numerador / denominador
b = media_cotacao - m * media_dias

print("Fórmulas utilizadas para o coeficiente angular e intercepto da regressão linear: m = Σ[(xi - x_média) * (yi - y_média)] / Σ[(xi - x_média)^2], b = y_média - m * x_média")

# Prever a Cotação para o próximo dia
cotacao_prevista = m * (len(dias) + 1) + b

print("Fórmula utilizada para a previsão linear: y = m * x + b")

# Resultados
print("\nDetalhes e Resultados:")
print(f"A equação da reta de tendência linear é: y = {m}x + {b}")
print(f"O valor previsto para o próximo dia é igual a {cotacao_prevista:.6f}")
