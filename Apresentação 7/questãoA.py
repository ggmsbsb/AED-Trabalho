import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

# Dados fornecidos
data = {
    'Ano': [2015, 2016, 2017, 2018, 2019, 2020, 2021, 2022, 2023, 2024],
    'Índice Gini': [0,496300241, 0,519534818, 0,586416119, 0,601124934, 0,542588302, 0,494670229, 0,526021771, 0,591726337, 0,597650597, 0,535307008]
}

# Corrigir valores decimais
data['Índice Gini'] = [0.496300241, 0.519534818, 0.586416119, 0.601124934, 0.542588302, 0.494670229, 0.526021771, 0.591726337, 0.597650597, 0.535307008]

# Criar DataFrame
df = pd.DataFrame(data)

# Definir variáveis independentes e dependentes
X = df[['Ano']]
y = df['Índice Gini']

# Criar e ajustar o modelo de regressão linear
# Regressão Linear: y = a + bx
model = LinearRegression()
model.fit(X, y)

# Gerar a equação da linha de tendência
coef = model.coef_[0]
intercept = model.intercept_
equacao_tendencia = f"Índice Gini = {coef:.6f} * Ano + {intercept:.6f}"

# Prever o índice Gini para 2025
ano_previsto = 2025
gini_previsto = model.predict([[ano_previsto]])[0]

# Calcular valores previstos e relativo cíclico
#Rel Cicli = (Índice Gini / Gini Previsto) * 100
df['Gini Previsto'] = model.predict(X)
df['Relativo Cíclico (%)'] = 100 * df['Índice Gini'] / df['Gini Previsto']

# Determinar se o país terá acesso à assistência internacional
assistencia_internacional = "terá acesso à assistência internacional" if gini_previsto > 0.6 else "NÃO terá acesso à assistência internacional"

# Resultados
print(f"A equação de tendência linear é: {equacao_tendencia}")
print(df)
print(f"O valor previsto para o ano de 2025 é igual a {gini_previsto:.6f}")
print(f"O país {assistencia_internacional}")

# Plotando os dados e a linha de tendência
plt.figure(figsize=(10, 6))
plt.scatter(df['Ano'], df['Índice Gini'], color='blue', label='Índice Gini Observado')
plt.plot(df['Ano'], df['Gini Previsto'], color='red', label='Linha de Tendência Linear')
plt.xlabel('Ano')
plt.ylabel('Índice Gini')
plt.title('Tendência do Índice Gini')
plt.legend()
plt.grid(True)
plt.show()
