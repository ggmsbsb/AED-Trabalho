import numpy as np
from scipy.stats import chisquare, chi2

# Entrada dos dados
marcas = ['1', '2', '3']
quantidades = [50, 30, 70]
total = sum(quantidades)

# Entrada do nível de significância
nivel_significancia = float(input("Digite o nível de significância (na questão A era de 1%): "))

# Valores esperados para uma distribuição uniforme
esperado = [total / len(quantidades)] * len(quantidades)

# Cálculo do teste qui-quadrado
estatistica_teste, p_valor = chisquare(quantidades, f_exp=esperado)

# Valor crítico da distribuição qui-quadrado
graus_de_liberdade = len(quantidades) - 1
valor_critico = chi2.ppf(1 - nivel_significancia, graus_de_liberdade)

# Saída dos resultados
print(f"O valor da estatística de teste é igual a {estatistica_teste:.4f}")
print(f"A confiança do teste é igual a {1 - nivel_significancia:.4f}")
print(f"O valor crítico da distribuição associada é igual a {valor_critico:.4f}")

# Decisão do teste
if estatistica_teste > valor_critico:
    print("A hipótese/afirmação dada deve ser rejeitada.")
else:
    print("A hipótese/afirmação dada deve ser aceita.")

#Prints de teste, pode ignorar isso aq
#print(p_valor)
#print(esperado)