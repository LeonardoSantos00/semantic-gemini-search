import os
from dotenv import load_dotenv

#Força o python a encontrar em qual pasta este arquivo ta
diretorio_atual = os.path.dirname(os.path.abspath(__file__))
caminho_env = os.path.join(diretorio_atual, '.env')

load_dotenv(caminho_env)

chave_secreta = os.getenv("GEMINI_API_KEY")

if chave_secreta:
    print("SUCESSO! A chave:", chave_secreta[:5] + " foi encontrada...")
else:
    print("ERRO")