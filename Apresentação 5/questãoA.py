import pandas as pd
from scipy.stats import f_oneway
import scipy.stats as stats

# Dados de produção em sacas de 60kg para cada fertilizante nas três regiões
data = {
    'Fertilizante 1': [30, 35, 25],
    'Fertilizante 2': [32, 31, 42],
    'Fertilizante 3': [26, 29, 26]
}

# Criar DataFrame
df = pd.DataFrame(data)

# Perguntar ao usuário o nível de significância
alpha = float(input("Digite o nível de significância (ex: 0.05): "))

# Calcular ANOVA
f_statistic, p_value = f_oneway(df['Fertilizante 1'], df['Fertilizante 2'], df['Fertilizante 3'])

# Número de grupos e número total de observações
k = len(data)
N = df.size

# Graus de liberdade
df_between = k - 1
df_within = N - k

# Valor crítico da distribuição F para os graus de liberdade e o nível de significância dado
f_critical = stats.f.ppf(1 - alpha, df_between, df_within)

# Mensagens de saída
print(f"O valor da estatística de teste é igual a {f_statistic:.4f}")
print(f"A confiança do teste é igual a {1 - alpha:.2%}")
print(f"O valor crítico da distribuição associada é igual a {f_critical:.4f}")

# Decisão sobre a hipótese nula
if f_statistic > f_critical:
    print("A hipótese/afirmação dada deve ser rejeitada.")
else:
    print("A hipótese/afirmação dada deve ser aceita.")
