import json

#JSON PATH (Fica de olho pq isso --> VAI <-- mudar de acordo com o seu diretório)
json_path = r"D:\CDMI\AEDTRAB\dados\acoes.json"

# Abrindo o arquivo JSON e carregando os dados
with open(json_path, "r") as arquivo:
    dados = json.load(arquivo)

dias = dados["dias"]

#Printando os dados só pra testar
#print(dias)