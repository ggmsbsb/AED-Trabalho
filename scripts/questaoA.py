import json
import numpy as np
from scipy import stats

#Acessa o arquivo JSON e carrega os dados.
def carregar_dados(caminho_arquivo):
    with open(caminho_arquivo, "r") as arquivo:
        dados = json.load(arquivo)
    return [dia["valor"] for dia in dados["dias"]]

#Calcula a média dos valores.
def calcular_media(valores): #VERMELHO
    return np.mean(valores)

#Calcula o desvio padrão dos valores.
def calcular_desvio_padrao(valores): #AZUL
    return np.std(valores, ddof=1)#ddof = grau de liberdade | std = Standard Deviation

#Calcula o intervalo de confiança. Nível especificado no enunciado (95%).
def calcular_intervalo_confianca(media, desvio_padrao, nivel_confianca=0.95):  #VERDE
    return stats.norm.interval(nivel_confianca, loc=media, scale=desvio_padrao)

def main():
    # JSON PATH fica de olho pq isso --> VAI <-- mudar de acordo com o seu PC.
    json_path = r"D:\CDMI\AEDTRAB\dados\acoes.json"

    # Carregar os dados
    valores = carregar_dados(json_path)

    #Calculos(Só passar o mouse nas cores pra ver a função responsavel por cada uma.)
    media = calcular_media(valores) #VERMELHO
    desvio_padrao = calcular_desvio_padrao(valores) #AZUL
    intervalo_confianca = calcular_intervalo_confianca(media, desvio_padrao) #VERDE

    # Valor ideal para compra e venda
    valor_compra = intervalo_confianca[0] #Limite mais baixo do intervalo de confiança.
    valor_venda = intervalo_confianca[1] #Limite mais alto do intervalo de confiança.

    #Lucro previsto =  Valor ideal para venda−Valor ideal para compra
    lucro_previsto = valor_venda - valor_compra

    # Exibindo os valores ideais para compra e venda
    #Questão A - A
    print(f"Valor ideal para compra: R${valor_compra:.2f}")
    print(f"Valor ideal para venda: R${valor_venda:.2f}")
    #Questão A - B
    print(f"Lucro previsto: R${lucro_previsto:.2f}")


#Executa a função main
if __name__ == "__main__":
    main()
