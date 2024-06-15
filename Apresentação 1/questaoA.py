import numpy as np

# Série histórica dos valores do ativo financeiro
serie = [
    {"dia": "1", "valor": 15.01},
    {"dia": "2", "valor": 18.92},
    {"dia": "3", "valor": 20.00},
    {"dia": "4", "valor": 15.78},
    {"dia": "5", "valor": 17.17},
    {"dia": "6", "valor": 16.23},
    {"dia": "7", "valor": 18.23},
    {"dia": "8", "valor": 18.00},
    {"dia": "9", "valor": 17.88},
    {"dia": "10", "valor": 19.02}
]

# Extraindo os valores em uma lista
valores = [dia['valor'] for dia in serie]

# Calculando a soma dos valores
soma_valores = sum(valores)

# Calculando média móvel de 10 dias
media_10d = soma_valores / len(valores)

# Calculando a média da série histórica
media = soma_valores / len(valores)

# Calculando o desvio padrão da série histórica
soma_diferencas_quadradas = sum((x - media) ** 2 for x in valores)
desvio_padrao = np.sqrt(soma_diferencas_quadradas / (len(valores) - 1))

# Calculando intervalo de confiança bilateral de 95%
z_score = 1.96  # Valor de Z para 95% de confiança
intervalo_confianca = z_score * (desvio_padrao / np.sqrt(len(valores)))

# Determinando valores extremos para compra e venda de ações
valor_compra = media - intervalo_confianca
valor_venda = media + intervalo_confianca

# Calculando quantidade de ações adquiridas com base no capital inicial
capital_inicial = 1000000
quantidade_acoes = int(np.floor(capital_inicial / valor_compra))

# Calculando lucro previsto com base nos valores de compra e venda
lucro_previsto = quantidade_acoes * (valor_venda - valor_compra)

# Exibindo resultados
print(f"Valor ideal para compra: R${valor_compra:.2f}")
print(f"Valor ideal para venda: R${valor_venda:.2f}")
print(f"Quantidade de ações adquiridas: {quantidade_acoes}")
print(f"Lucro obtido previsto: R${lucro_previsto:.2f}")

# Exibindo todos os valores utilizados em forma de tabela
print("\nValores Utilizados:")
for i, valor in enumerate(valores, 1):
    print(f"X{i}: {valor:.2f}", end=" | ")
print(f"\n\nSoma dos valores (ΣX): {soma_valores}")
print(f"Média dos valores (X̄): {media}")
print(f"Soma das diferenças quadradas: {soma_diferencas_quadradas}")
print(f"Desvio padrão (σ): {desvio_padrao}")
print(f"Z-Score (95% confiança): {z_score}")
print(f"Intervalo de confiança: {intervalo_confianca}")
print(f"Valor de compra: {valor_compra}")
print(f"Valor de venda: {valor_venda}")
print(f"Capital inicial: {capital_inicial}")
print(f"Quantidade de ações: {quantidade_acoes}")
print(f"Lucro previsto: {lucro_previsto}")
