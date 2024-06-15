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

# Mostrar tabela de valores X e Y, e calcular soma de X e Y
print("Tabela de Dados:")
print(df.to_string(index=False))

# Calcular soma de X e Y
soma_X = df.sum(axis=0)
soma_Y = df.sum(axis=1)

# Calcular ANOVA
estatistica_F, p_valor = f_oneway(df['Fertilizante 1'], df['Fertilizante 2'], df['Fertilizante 3'])

# Número de grupos e número total de observações
k = len(data)
N = df.size

# Graus de liberdade
df_entre_grupos = k - 1
df_dentro_grupos = N - k

# Perguntar ao usuário o nível de significância
alpha = float(input("Digite o nível de significância (ex: 0.05): "))

# Valor crítico da distribuição F para os graus de liberdade e o nível de significância dado
f_critico = stats.f.ppf(1 - alpha, df_entre_grupos, df_dentro_grupos)

# Supondo que as variáveis soma_Y, estatistica_F, p_valor, k, N, df_entre_grupos, df_dentro_grupos e f_critico já foram definidas
print(f"Soma de Y (total por região): {soma_Y}")
print(f"Valor da estatística de teste (F): {estatistica_F:.4f}")
print(f"P-valor: {p_valor:.4f}")
print(f"Número de grupos (k): {k}")
print(f"Número total de observações (N): {N}")
print(f"Graus de liberdade entre grupos: {df_entre_grupos}")
print(f"Graus de liberdade dentro dos grupos: {df_dentro_grupos}")
print(f"Valor crítico da distribuição F: {f_critico:.4f}")

print("Fórmula utilizada para a estatística F: F = MS_entre / MS_dentro")
print("Fórmula utilizada para os graus de liberdade entre grupos: df_entre_grupos = k - 1")
print("Fórmula utilizada para os graus de liberdade dentro dos grupos: df_dentro_grupos = N - k")

# Decisão sobre a hipótese nula
if estatistica_F > f_critico:
    print("\nRejeitar a hipótese nula: há diferença significativa entre os grupos.")
else:
    print("\nAceitar a hipótese nula: não há diferença significativa entre os grupos.")
