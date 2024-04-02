import json
import numpy as np
from scipy import stats

# Função para carregar os dados do arquivo JSON e extrair os valores dos dias.
def carregar_dados(caminho_arquivo):
    try:
        with open(caminho_arquivo, "r") as arquivo:
            dados = json.load(arquivo)
        return [dia["valor"] for dia in dados["dias"]]
    except FileNotFoundError:
        print(f"Verificar se o caminho do arquivo está correto: {caminho_arquivo}")
        return []

# Função para calcular a média móvel dos últimos N dias
def calcular_media_movel(valores, N):
    return np.convolve(valores, np.ones(N)/N, mode='valid')

# Função para calcular o desvio padrão móvel dos últimos N dias
def calcular_desvio_padrao_movel(valores, N):
    return [np.std(valores[i-N:i], ddof=1) for i in range(N, len(valores)+1)]

def main():
    # JSON PATH (Fica de olho pq isso --> VAI <-- mudar de acordo com o seu diretório)
    json_path = r"D:\CDMI\AEDTRAB\dados\acoes.json"

    # Carregar os dados
    valores = carregar_dados(json_path)

    # Número de dias para considerar para a média móvel e o desvio padrão móvel
    N = 10

    # Calcular média móvel e desvio padrão móvel
    media_movel = calcular_media_movel(valores, N)
    desvio_padrao_movel = calcular_desvio_padrao_movel(valores, N)

    # Calcular valores de compra e venda dinâmicos para cada dia
    valor_compra = [avg - std for avg, std in zip(media_movel, desvio_padrao_movel)]
    valor_venda = [avg + std for avg, std in zip(media_movel, desvio_padrao_movel)]

    # Exibindo os valores ideais para compra e venda para cada dia
    for dia, (compra, venda) in enumerate(zip(valor_compra, valor_venda), 1):
        print(f"Dia {dia}: Valor ideal para compra: R${compra:.2f}, Valor ideal para venda: R${venda:.2f}")

if __name__ == "__main__":
    main()
