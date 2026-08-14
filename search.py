import requests
import os
from google import genai

from dotenv import load_dotenv

#Força o python a encontrar em qual pasta este arquivo ta
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_env = os.path.join(diretorio_atual, '.env')

load_dotenv(caminho_env)

chave_secreta = os.getenv("GEMINI_API_KEY")

if chave_secreta:
    print("SUCESSO! A chave:", chave_secreta[:4] + " foi encontrada...")
else:
    print("ERRO")

while True:
    produto = input("\nQual produto deseja buscar? (ou digite 'sair' para encerrar): ")

    if produto.lower().strip() == 'sair':
        print("Encerrando o programa...")
        break

    if not produto.strip():
        print("Busca vazia. Tente novamente.")
        continue

    url_final = f"https://dummyjson.com/products/search?q={produto}"

    print(f"Buscando por: {produto}....")

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

            prompt = f"Você é um assistente de vendas inteligente. Convença o cliente a comprar o produto {primeiro_item['title']} que custa ${primeiro_item['price']}. Seja persuaviso e diga que é uma ótima oportunidade."
            client = genai.Client(api_key=chave_secreta)

            resposta_ia = client.models.generate_content(
                model='gemini-3.5-flash-lite',
                contents=prompt
            )

            print("\n---RESPOSTA DA IA ---")
            print(resposta_ia.text)
        else:
            print("Nenhum produto encontrado com esse nome")
    else:
        print(f"Erro na busca. Código HTTP:{resposta.status_code}")
