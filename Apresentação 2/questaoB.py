import math
from scipy.stats import norm

# Dados da amostra
media_amostral = 4000  # média da amostra em horas
desvio_padrao_amostral = 200  # desvio padrão da amostra em horas
n = 10  # tamanho da amostra

# Cálculo do Z-score para um intervalo de confiança de 95%
Z = norm.ppf(0.95)

# Cálculo do intervalo de confiança
intervalo_confianca = Z * desvio_padrao_amostral / math.sqrt(n - 1)
limite_inferior = media_amostral - intervalo_confianca
limite_superior = media_amostral + intervalo_confianca

# Vida útil estimada
vida_util_estimada = media_amostral

# Intervalo de confiança para a vida útil
limite_inferior_vida_util = limite_inferior
limite_superior_vida_util = limite_superior

# Impressão dos resultados
print("\nEstimativa da vida útil")
print(f"Vida útil estimada: {vida_util_estimada:.2f} horas")
print("Intervalo de confiança para a vida útil:")
print(f"Limite inferior: {limite_inferior_vida_util:.2f} horas")
print(f"Limite superior: {limite_superior_vida_util:.2f} horas")
