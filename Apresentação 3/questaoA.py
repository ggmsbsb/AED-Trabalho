import numpy as np
import pandas as pd
from scipy import stats

# Definir os dados
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
taxa_selic = [0.73, 0.76, 0.93, 0.83, 1.03, 1.02, 1.03, 1.17, 1.07, 1.02, 1.02, 1.12]
taxa_ipca =  [0.54, 1.01, 1.62, 1.06, 0.47, 0.67, -0.68, -0.36, -0.29, 0.59, 0.41, 0.62]

# Criar um DataFrame
df = pd.DataFrame({'meses': meses, 'taxa_selic': taxa_selic, 'taxa_ipca': taxa_ipca})

# Calcular a correlação móvel trimestral
df['correlacao'] = df['taxa_selic'].rolling(window=3).corr(df['taxa_ipca'])

# Solicitar ao usuário que insira o nível de significância
alpha = float(input("Insira o nível de significância: "))

# Realizar um teste t. A formula utilizada é t = (x̄ - μ) / (s / Raiz de n).
t_stat, p_val = stats.ttest_1samp(df['correlacao'].dropna(), 0) #O teste T

# Imprimir os resultados
print(f"O valor da estatística de teste é igual a {t_stat}")
print(f"A confiança do teste é igual a {1 - p_val}")
print(f"O valor crítico da distribuição associada é igual a {stats.t.ppf(1 - alpha, df=df['correlacao'].dropna().count() - 1)}")
if p_val < alpha:
    print("A hipótese/afirmação dada deve ser rejeitada")
else:
    print("A hipótese/afirmação dada deve ser aceita")