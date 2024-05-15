import numpy as np
from scipy.stats import pearsonr, t

# Dados fornecidos na tabela
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
taxa_selic = [0.73, 0.76, 0.93, 0.83, 1.03, 1.02, 1.03, 1.17, 1.07, 1.02, 1.02, 1.12]
taxa_ipca =  [0.54, 1.01, 1.62, 1.06, 0.47, 0.67, -0.68, -0.36, -0.29, 0.59, 0.41, 0.62]

# Calcula o coeficiente de correlação e o p-valor entre a taxa SELIC e o IPCA
coeficiente_correlacao, p_valor = pearsonr(taxa_selic, taxa_ipca)

# Define o nível de significância
significancia = float(input("Digite o nível de significância (0-1): "))

# Calcula o valor crítico usando o nível de significância e o tamanho da amostra
n = len(taxa_selic)
valor_critico = t.ppf(1 - significancia/2, n - 2)

# Calcula o valor da estatística de teste utilizando a fórmula t = (X̄ - μ) / (s/√n). Dada na utlma aula.
media_taxa_selic = np.mean(taxa_selic)
media_taxa_ipca = np.mean(taxa_ipca)
desvio_padrao_taxa_selic = np.std(taxa_selic, ddof=1)  # Usamos ddof=1 para calcular o desvio padrão amostral
teste_t = (media_taxa_selic - media_taxa_ipca) / (desvio_padrao_taxa_selic / np.sqrt(n))

# Imprime os resultados
print(f"O valor da estatística de teste é igual a {teste_t:.2f}")
print(f"A confiança do teste é igual a {1 - significancia:.2f}")
print(f"O valor crítico da distribuição associada é igual a {valor_critico:.2f}")

# Teste de hipótese
if np.abs(teste_t) > valor_critico:
    print("A hipótese/afirmação dada deve ser rejeitada.")
else:
    print("A hipótese/afirmação dada pode ser aceita.")


