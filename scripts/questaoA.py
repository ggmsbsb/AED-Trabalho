import json
import numpy as np
from scipy import stats

# Acessa o arquivo JSON e carrega os dados.
def carregar_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
        return [dia["valor"] for dia in dados["dias"]]
    except FileNotFoundError:
        print(f"Por favor, verifique se o caminho do arquivo está correto: {caminho_arquivo}")
        return []

# Calcula a média móvel dos últimos N dias
def calcular_media_movel(valores, N):
    return np.convolve(valores, np.ones(N)/N, mode='valid')

# Calcula o desvio padrão dos últimos N dias
def calcular_desvio_padrao(valores, N):
    return [np.std(valores[i-N:i], ddof=1) for i in range(N, len(valores)+1)]

def main():
    # Caminho do JSON
    caminho_json = r"D:\CDMI\AEDTRAB\dados\acoes.json"

    # Carrega os dados
    valores = carregar_dados(caminho_json)

    # Número de dias a serem considerados para média móvel e desvio padrão móvel
    N = 10
    media_movel = calcular_media_movel(valores, N)
    desvio_padrao_movel = calcular_desvio_padrao(valores, N)

    # Preços de compra e venda dinâmicos para cada dia
    valor_compra = [media - desvio for media, desvio in zip(media_movel, desvio_padrao_movel)]
    valor_venda = [media + desvio for media, desvio in zip(media_movel, desvio_padrao_movel)]
    
    # Inicializa o número de ações compradas e o lucro total
    num_acoes = 0
    lucro_total = 0.0
    capital = 1000000  # Capital inicial
    melhor_preco_compra = float('inf')  # Inicializa o melhor preço de compra como infinito
    maior_preco_venda = 0  # Inicializa o maior preço de venda como 0

    # Percorre os preços para cada dia
    for dia, preco in enumerate(valores):
        if preco < melhor_preco_compra:
            melhor_preco_compra = preco
            if capital >= melhor_preco_compra:
                num_acoes_compradas = capital // melhor_preco_compra
                capital -= num_acoes_compradas * melhor_preco_compra
                num_acoes += num_acoes_compradas

        if preco > maior_preco_venda and num_acoes > 0:
            maior_preco_venda = preco

    # Calcula o lucro
    lucro_total = num_acoes * (maior_preco_venda - melhor_preco_compra)
    capital += num_acoes * maior_preco_venda

    # Imprime os resultados
    print(f"Melhor Preço de Compra = {melhor_preco_compra:.2f}, Maior Preço de Venda = {maior_preco_venda:.2f}, Número de Ações Compradas = {num_acoes}, Lucro Esperado = {lucro_total:.2f}")

    num_acoes = 0  # Reseta o número de ações compradas

if __name__ == "__main__":
    main()