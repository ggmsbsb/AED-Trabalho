import numpy as np
import pandas as pd
from scipy.stats import t

# Definir os dados
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
taxa_selic = [0.73, 0.76, 0.93, 0.83, 1.03, 1.02, 1.03, 1.17, 1.07, 1.02, 1.02, 1.12]
taxa_ipca =  [0.54, 1.01, 1.62, 1.06, 0.47, 0.67, -0.68, -0.36, -0.29, 0.59, 0.41, 0.62]

# Criar um DataFrame
df = pd.DataFrame({'mês': meses, 'taxa_selic': taxa_selic, 'taxa_ipca': taxa_ipca})

# Calcular a correlação móvel trimestral
df['correlacao'] = df['taxa_selic'].rolling(window=3).corr(df['taxa_ipca'])

# Solicitar ao usuário que insira o nível de significância
alpha = float(input("Insira o nível de significância: "))

# Calcular estatística de teste t para correlação
correlacao = df['correlacao'].dropna()
x_bar = correlacao.mean()
mu = 0
s = correlacao.std()
n = len(correlacao)
t_stat = (x_bar - mu) / (s / np.sqrt(n))

# Calcular p-valor usando a distribuição t de Student
p_val = t.sf(np.abs(t_stat), n - 1) * 2

# Imprimir os resultados
print("\nFórmulas Utilizadas:")
print("1. Cálculo da estatística de teste t para correlação:")
print("   t_stat = (x_bar - mu) / (s / sqrt(n))")
print("2. Cálculo do p-valor:")
print("   p_val = t.sf(abs(t_stat), n-1) * 2")

# Tabela de Valores X e Y
print("\nTabela de Valores X e Y:")
print("| Mês  | Taxa Selic | Taxa IPCA |")
print("|------|------------|-----------|")
total_selic = 0
total_ipca = 0
for i in range(len(meses)):
    total_selic += taxa_selic[i]
    total_ipca += taxa_ipca[i]
    print(f"| {meses[i]} | {taxa_selic[i]:.2f} | {taxa_ipca[i]:.2f} |")

# Imprimir a soma dos valores
print(f"\nSoma dos valores da tabela:")
print(f"Total Taxa Selic: {total_selic:.2f}")
print(f"Total Taxa IPCA: {total_ipca:.2f}")

# Tabela de Valores Utilizados nos Cálculos
print("\nValores Utilizados nos Cálculos:")
print("| Variável                       | Valor    |")
print("|--------------------------------|----------|")
print(f"| Média Amostral da Correlação   | {x_bar:.4f} |")
print(f"| Média Populacional (mu)        | {mu}       |")
print(f"| Desvio Padrão da Correlação    | {s:.4f}   |")
print(f"| Tamanho da Amostra (n)         | {n}       |")
print(f"| Estatística de Teste (t_stat)  | {t_stat:.4f} |")
print(f"| P-valor                        | {p_val:.4f} |")
print(f"| Nível de Significância (alpha) | {alpha}   |")

# Determinar se a hipótese nula deve ser rejeitada ou não
print("\nResultado do Teste de Correlação:")
print(f"A confiança do teste é igual a {(1 - alpha) * 100}%")
print(f"O valor crítico da distribuição associada é igual a {t.ppf(1 - alpha, df=n - 1):.4f}")
if p_val < alpha:
    print("Conclusão: A hipótese nula de não correlação deve ser rejeitada")
else:
    print("Conclusão: A hipótese nula de não correlação não deve ser rejeitada")
