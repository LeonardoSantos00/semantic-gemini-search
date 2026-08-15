# semantic-gemini-search
Assistente inteligente de buscas semânticas em linguagem natural, integrando o consumo de APIs públicas dinâmicas com a IA do Google Gemini

---

## Sobre o Projeto

Este projeto foi desenvolvido como resolução de um Desafio Prático para Orientação de TCC. A aplicação consome dados em tempo real de um e-commerce simulado e utiliza Inteligência Artificial para atuar como um consultor de vendas, apresentando os produtos de forma a convencer e baseada em dados reais.

### Qual API Pública foi escolhida e por quê?
Foi utilizada a API **DummyJSON** (`https://dummyjson.com`)

**Motivo:** Inicialmente, o objetivo era utilizar a API do Mercado Livre, pois a intenção era criar uma ferramenta útil para o meu dia a dia, como um assistente para analisar qual celular topo de linha oferece o melhor custo-benefício. No entanto, após realizar as primeiras requisições, esbarrei no erro HTTP 403, pois a plataforma fechou endpoints públicos e agora exige tokens de autenticação complexos (OAuth 2.0) até para buscas simples.

Diante desse bloqueio, pivotei para a API DummyJSON por ser a alternativa ideal para manter a arquitetura planejada. Ela simula perfeitamente um e-commerce real e não possui barreiras de autenticação, entregando um JSON rico em detalhes (descontos, avaliações, estoque). Essa estrutura exigiu um tratamento e filtragem de dados minucioso, e forneceu o contexto ideal para a IA trabalhar de forma fundamentada, sem alucinações.

---

## Como Executar o Projeto

**1. Clone o repositório**
```bash
git https://github.com/LeonardoSantos00/semantic-gemini-search.git
```

**2. Crie e ative o ambiente virtual**
```bash
# Crie o ambiente
python3 -m venv venv

# Ative no Linux/macOS
source venv/bin/activate 

# Ou ative no Windows
venv\Scripts\activate
```

**3. Instale as dependências**
```bash
pip install -r requirements.txt
```

**4. Configure as credenciais de segurança**
Na raiz do projeto, crie um arquivo chamado `.env` e insira a sua chave do Google AI Studio no formato abaixo:
```text
GEMINI_API_KEY=sua_chave_secreta_aqui
```

**5. Inicie a aplicação**
```bash
python3 search.py
```

---

## Exemplo Prático
O sistema roda em um loop interativo aguardando os inputs do usuário. Abaixo, um exemplo de busca e resposta do assistente:

**Input:**
```text
Qual produto deseja buscar? (ou digite 'sair' para encerrar): watch
Buscando por: watch....
```

**Output:**
```text
---RESULTADO DA BUSCA---
Produto encontrado: Brown Leather Belt Watch
Preço: \$89.99 (Desconto atual: 5.99%)
Estoque: 32 unidades | Avaliação: 4.19 estrelas

---RESPOSTA DA IA ---
Olá. Seja bem-vindo.

Apresento a você o relógio Brown Leather Belt Watch. O preço final deste produto é de 89.99 dólares. No momento, contamos com uma vantagem promocional que oferece um desconto de 5.99 por cento sobre o valor.

Este modelo é um relógio estiloso com um design clássico. Ele possui uma pulseira de couro genuíno e um mostrador elegante, adicionando um toque de sofisticação ao seu visual.

Em termos de reputação, a avaliação média dos clientes para este item é de 4.19 estrelas. Atualmente, temos 32 unidades disponíveis em nosso estoque.
```
