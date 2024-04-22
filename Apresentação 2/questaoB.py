import math
from scipy.stats import norm

# Dados da amostra
media_amostral = 4000  # média da amostra em horas
desvio_padrao_amostral = 200  # desvio padrão da amostra em horas
n = 10  # tamanho da amostra

# Cálculo do Z-score para um intervalo de confiança de 95%
Z = norm.ppf(0.95)

# Cálculo do intervalo de confiança
intervalo_confianca = Z * (desvio_padrao_amostral / math.sqrt(n))
limite_inferior = media_amostral - intervalo_confianca
limite_superior = media_amostral + intervalo_confianca

# Impressão dos resultados
print(f"Intervalo de confiança de 95%: ({limite_inferior:.2f}, {limite_superior:.2f}) horas")
