import numpy as np
from scipy.stats import ttest_ind, t

# Dados fornecidos na tabela
meses = ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez']
selic = [0.73, 0.76, 0.93, 0.83, 1.03, 1.02, 1.03, 1.17, 1.07, 1.02, 1.02, 1.12]
ipca = [0.54, 1.01, 1.62, 1.06, 0.47, 0.67, -0.68, -0.36, -0.29, 0.59, 0.41, 0.62]

def teste_hipotese(nivel_de_significancia):
    # Calcula a estatística de teste (por exemplo, t-teste)
    estatistica_de_teste, valor_p = ttest_ind(selic, ipca)

    # Calcula o nível de confiança
    confianca = 1 - nivel_de_significancia

    # Calcula o valor crítico
    df = len(selic) + len(ipca) - 2  # graus de liberdade
    valor_critico = t.ppf(1 - nivel_de_significancia / 2, df)

    # Decide se aceita ou rejeita a hipótese
    if abs(estatistica_de_teste) > valor_critico:
        resultado = "rejeitada"
    else:
        resultado = "aceita"

    # Imprime os resultados
    print(f"O valor da estatística de teste é igual a {estatistica_de_teste}")
    print(f"A confiança do teste é igual a {confianca}")
    print(f"O valor crítico da distribuição associada é igual a {valor_critico}")
    print(f"A hipótese/afirmação dada deve ser {resultado}")

# Chama a função com um nível de significância fornecido pelo usuário
nivel_de_significancia = float(input("Insira o nível de significância: "))
teste_hipotese(nivel_de_significancia)

# NÃO ENTENDI A MATÉRIA DIREITO, ENTÃO NÃO SEI SE ESTÁ CERTO