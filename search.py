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

        print("\n---RESULTADO DA BUSCA---")

        if "products" in dados and len(dados["products"]) > 0:
            item = dados["products"][0]

            titulo = item['title']
            preco = item['price']
            estoque = item['stock']
            descricao = item.get('description', 'Produto exclusivo e sem descrição detalhada.')
            avaliacao = item.get('rating', 'Ainda não avaliado.')
            desconto = item.get('discountPercentage', 0)

            print(f"Produto encontrado: {titulo}")

            if desconto > 0:
                print(f"Preço: ${preco} (Desconto atual: {desconto}%)")
            else:
                print(f"Preço: ${preco}")
            
            print(f"Estoque: {estoque} unidades | Avaliação: {avaliacao} estrelas")

            prompt = (
                f"Você é um consultor de vendas honesto e objetivo, não precisa dizer que é, apenas aja como um consultor.Dê uma pequena saudação."
                f" Apresente o produto '{titulo}' cujo preço final é ${preco}. Se o desconto ({desconto}%) for maior que zero, mencione-o "
                f"como uma vantagem, mas NÃO tente calcular o preço original. "
                f"Use a descrição ({descricao}) para explicar a utilidade do produto. "
                f"Informe de maneira neutra que a avaliação média é de {avaliacao} estrelas e que "
                f"temos {estoque} unidades disponíveis. Não crie falsos sensos de urgência e não invente dados"
            )

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
