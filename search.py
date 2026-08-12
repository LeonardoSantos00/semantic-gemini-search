import requests

#produto = "Cadeira Ergonômica de Escritório"
produto = "laptop"
#url_base = "https://api.mercadolibre.com/sites/MLB/search?q="
#url_final = url_base + produto #Juntar os dois para formar a rota da viagem
url_final = f"https://dummyjson.com/products/search?q={produto}"

print(f"Buscando por: {produto}....")

#Adicionando um Header para disfarçar o script e o Meli não barrar
#cabecalho = {
#    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
#}

resposta = requests.get(url_final)

if resposta.status_code == 200:
    print("Sucesso! A API respondeu")
    dados = resposta.json() #é um hashmap simplificado

    print("\n---RESULTADO DO GARIMPO---")
    
    if "products" in dados and len(dados["products"]) > 0:
        primeiro_item = dados["products"][0]
        print(f"Produto encontrado: {primeiro_item['title']}")
        print(f"Preço: ${primeiro_item['price']}")
        print(f"Estoque: {primeiro_item['stock']} unidades")
    else:
        print("Nenhum produto encontrado com esse nome")
    #print("\nAs chaves principais do JSON recebido são: ")
    #print(dados.keys())
else:
    print(f"Erro na busca. Código HTTP:{resposta.status_code}")
    #print(f"Motivo que o servidor deu foi: {resposta.text}")
