import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression

data = ['01/08', '02/08', '03/08', '04/08', '05/08', '08/08', '09/08', '10/08', '11/08', '12/08', '15/08', '16/08', '17/08', '18/08', '19/08', '22/08', '23/08', '24/08', '25/08', '26/08', '29/08', '30/08', '31/08' ]
cotacao = [5.21, 5.26, 5.29, 5.29, 5.26, 5.23, 5.16, 5.09, 5.06, 5.02, 5.01, 5, 5.03, 5.08, 5.15, 5.21, 5.26, 5.31, 5.29, 5.27, 5.23, 5.18, 5.11]

df = pd.DataFrame({'Data': data, 'Cotacao': cotacao})

#Convertendo a coluna Data para datetime
df['Data'] = pd.to_datetime(df['Data'], format='%d/%m').dt.strftime('%d/%m')
#Adicionando uma coluna com os dias corridos para facilitar a regressao linear
dias = ['1', '2', '3', '4', '5', '8', '9', '10', '11', '12', '15', '16', '17', '18', '19', '22', '23', '24', '25', '26', '29', '30', '31']
df['Dias'] = dias

print("-----------------------------")
print("1)")
print(df)
print("-----------------------------")

#Realizando a regressão linear:
X = df['Dias'].values.reshape(-1, 1)
dias = np.array(dias, dtype=int)
y = df['Cotacao'].values
model = LinearRegression()
model.fit(X, y)
a = model.coef_[0]
b = model.intercept_

tendencia = a * dias + b
relativo_ciclico = 0.01 * (cotacao/tendencia)

df['Tendencia'] = tendencia
df['Relativo_Ciclico'] = relativo_ciclico

print("2) A equacao de regressao linear (cotacao = -0.0003 * dias + 5.1796) é:", tendencia)
print("3) O valor aproximado do coeficiente 'a' é igual a:", a)
print("4) O valor aproximado do coeficiente 'b' é igual a:", b)