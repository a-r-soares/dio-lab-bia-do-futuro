from openai import OpenAI
import requests
import os
from dotenv import load_dotenv

# Carrega as variáveis do arquivo .env para o sistema
load_dotenv()

# ==============================================================================
# BLOCO 1: EXTRAÇÃO DE DADOS (O "Batch Load" da API do Banco Central)
# ==============================================================================
tabela_indicadores = {
    "IPCA (Variação Mensal)": 433,
    "IPCA-15 (Variação Mensal)": 7478,
    "IGP-M (Variação Mensal)": 189,
    "INPC (Variação Mensal)": 188,
    "IPC-Fipe (Variação Mensal)": 193,
    "Taxa Selic Over": 11,
    "Taxa Selic Meta": 432,
    "Taxa CDI": 12
}

dados_extraidos = {}
print("Iniciando sistemas do ALDO...")
print("Extraindo dados oficiais do Banco Central...\n")

for nome_indicador, codigo_api in tabela_indicadores.items():
    url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo_api}/dados/ultimos/1?formato=json"
    try:
        resposta = requests.get(url)
        resposta.raise_for_status()
        registro = resposta.json()[0]
        dados_extraidos[nome_indicador] = f"{registro['valor']}% (Ref: {registro['data']})"
        print(f"[OK] {nome_indicador} atualizado.")
    except Exception as erro:
        dados_extraidos[nome_indicador] = "Dado indisponível no momento"
        print(f"[ERRO] Falha ao carregar {nome_indicador}: {erro}")

# Montando o bloco de texto invisível
cenario_oficial = "\nCENÁRIO ECONÔMICO OFICIAL ATUAL:\n"
for nome, valor in dados_extraidos.items():
    cenario_oficial += f"- {nome}: {valor}\n"

# ==============================================================================
# BLOCO 2: CONFIGURAÇÃO DO AGENTE ALDO (O System Prompt)
# ==============================================================================
# Instruções base (sem o cenário ainda)
instrucoes_base = """
PERSONA:
Você é o ALDO, um assistente financeiro especialista em indicadores econômicos fornecidos pelo Banco Central do Brasil. Você é didático, paciente e acessível.

DIRETRIZES DE DADOS:
Você receberá a cada interação um bloco de texto oculto chamado 'CENÁRIO ECONÔMICO OFICIAL ATUAL' contendo as taxas do dia. Baseie-se exclusivamente nos valores deste bloco para informar os índices ao cliente, referindo-se a eles de forma amigável como "a taxa atual" ou "o índice de hoje".

REGRAS (GUARDRAILS):
1. Responda ESTRITAMENTE sobre os valores numéricos e conceitos dos indicadores injetados no contexto. NUNCA utilize seu conhecimento prévio para responder sobre cargos, nomes de pessoas, estrutura institucional do Banco Central ou dados históricos.
2. NUNCA recomende investimentos ou qualquer decisão financeira. Apenas informe os índices, como funcionam e onde impactam.
3. Se o usuário perguntar sobre qualquer coisa que não seja um indicador econômico (incluindo nomes de diretores, notícias ou política), bloqueie dizendo: "Sou um assistente focado apenas em taxas e indicadores. Posso ajudar explicando como funciona a Selic ou o IPCA..."
4. Sempre pergunte se o cliente entendeu.
5. Utilize linguagem simples, como se explicasse para um amigo leigo.
"""

# A injeção dinâmica de variáveis (Juntando as regras com os dados do dia)
prompt_do_sistema = instrucoes_base + cenario_oficial


# ==============================================================================
# BLOCO 3: INTEGRAÇÃO COM O LLM (Comunicação com o LM Studio)
# ==============================================================================
# Apontando o cliente para a porta local do seu computador
cliente_ia = OpenAI(base_url=os.getenv("LM_STUDIO_URL"),
                    api_key=os.getenv("LM_STUDIO_KEY"))

print("\n" + "="*50)
print("ALDO está online e pronto para ajudar!")
print("="*50 + "\n")

# A pergunta simulada do usuário (aqui no futuro entrará a sua tela com Streamlit/HTML)
pergunta_usuario = "Para que serve a Taxa CDI e de quanto ela é?"
print(f"CLIENTE: {pergunta_usuario}\n")

print("ALDO está digitando...\n")

# Fazendo a chamada transacional para o modelo
resposta_ia = cliente_ia.chat.completions.create(
    # O nome exato não importa tanto aqui, o LM Studio usa o que estiver carregado na RAM
    model="modelo-local-lmstudio",
    messages=[
        {"role": "system", "content": prompt_do_sistema},
        {"role": "user", "content": pergunta_usuario}
    ],
    temperature=0.3,  # Temperatura baixa garante respostas mais focadas e menos alucinações
)

# Imprimindo a resposta final
texto_final = resposta_ia.choices[0].message.content
print(f"ALDO: {texto_final}")
