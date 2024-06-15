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
print("\nFórmulas utilizadas:")
print("1. Cálculo da estatística de teste qui-quadrado:")
print("   estatística_teste = sum((O_i - E_i)^2 / E_i)")
print("2. Cálculo do valor crítico da distribuição qui-quadrado:")
print(f"   valor_crítico = chi2.ppf(1 - {nivel_significancia}, graus_de_liberdade)")

# Tabela de Valores Observados e Esperados
print("\nTabela de Valores Observados e Esperados:")
print("| Marca | Quantidade Observada (O_i) | Quantidade Esperada (E_i) |")
print("|-------|-----------------------------|---------------------------|")
for i in range(len(marcas)):
    print(f"|   {marcas[i]}   |        {quantidades[i]}        |             {esperado[i]:.2f}             |")
print(f"\nSoma dos valores da tabela: {sum(quantidades)}")

# Tabela de Valores Utilizados nos Cálculos
print("\nValores Utilizados nos Cálculos:")
print("| Variável                   | Valor  |")

# Cálculo da estatística de teste qui-quadrado
estatistica_teste = sum((O_i - E_i) ** 2 / E_i for O_i, E_i in zip(quantidades, esperado))
print("| Estatística de teste qui-quadrado  | {:.4f} |".format(estatistica_teste))

# Cálculo do valor crítico da distribuição qui-quadrado
valor_critico = chi2.ppf(1 - nivel_significancia, graus_de_liberdade)
print("| Valor crítico             | {:.4f} |".format(valor_critico))

# Decisão sobre a hipótese nula
if estatistica_teste > valor_critico:
    print("\nRejeitar a hipótese nula: há diferença significativa entre as quantidades observadas e esperadas.")
else:
    print("\nAceitar a hipótese nula: não há diferença significativa entre as quantidades observadas e esperadas.")
