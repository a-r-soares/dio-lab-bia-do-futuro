import streamlit as st
import requests
from openai import OpenAI

# ==============================================================================
# CONFIGURAÇÃO DA PÁGINA (Interface Gráfica)
# ==============================================================================
st.set_page_config(page_title="ALDO - Assistente Financeiro", page_icon="📈")
st.title("📈 ALDO")
st.caption(
    "Seu assistente financeiro didático para indicadores oficiais do Banco Central.")

# ==============================================================================
# BLOCO 1: EXTRAÇÃO DE DADOS (Com Cache de Memória)
# ==============================================================================
# O decorator @st.cache_data(ttl=3600) mantém os dados em memória por 1 hora.
# Assim, o sistema não sobrecarrega a API do governo a cada interação na tela.


@st.cache_data(ttl=3600)
def carregar_dados_bcb():
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
    for nome, codigo in tabela_indicadores.items():
        url = f"https://api.bcb.gov.br/dados/serie/bcdata.sgs.{codigo}/dados/ultimos/1?formato=json"
        try:
            resposta = requests.get(url)
            resposta.raise_for_status()
            registro = resposta.json()[0]
            dados_extraidos[nome] = f"{registro['valor']}% (Ref: {registro['data']})"
        except Exception:
            dados_extraidos[nome] = "Dado indisponível no momento"

    cenario = "\nCENÁRIO ECONÔMICO OFICIAL ATUAL:\n"
    for n, v in dados_extraidos.items():
        cenario += f"- {n}: {v}\n"

    return cenario


# ==============================================================================
# BLOCO 2: CONFIGURAÇÃO DO AGENTE ALDO (System Prompt)
# ==============================================================================
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

# Carrega os dados na memória (vai na API apenas na 1ª vez)
prompt_do_sistema = instrucoes_base + carregar_dados_bcb()

# ==============================================================================
# BLOCO 3: GERENCIAMENTO DE SESSÃO E RENDERIZAÇÃO DO CHAT
# ==============================================================================
cliente_ia = OpenAI(base_url=st.secrets["BASE_URL"],
                    api_key=st.secrets["API_KEY"])

# Inicializa o histórico na memória da sessão se for o primeiro acesso
if "historico_chat" not in st.session_state:
    st.session_state.historico_chat = [
        {"role": "system", "content": prompt_do_sistema},
        {"role": "assistant",
            "content": "Olá! Eu sou o ALDO. Como posso te ajudar a entender a economia hoje?"}
    ]

# Renderiza todas as mensagens passadas na tela (ocultando a instrução do sistema)
for mensagem in st.session_state.historico_chat:
    if mensagem["role"] != "system":
        with st.chat_message(mensagem["role"]):
            st.markdown(mensagem["content"])

# ==============================================================================
# BLOCO 4: INTERAÇÃO COM O USUÁRIO (O Loop do Chatbot)
# ==============================================================================
# st.chat_input cria a barra de digitação no final da tela
if pergunta := st.chat_input("Pergunte sobre Selic, IPCA, CDI..."):

    # 1. Exibe a pergunta do usuário na tela e salva no histórico
    with st.chat_message("user"):
        st.markdown(pergunta)
    st.session_state.historico_chat.append(
        {"role": "user", "content": pergunta})

    # 2. Chama o LM Studio e exibe a resposta
    with st.chat_message("assistant"):
        # Um placeholder temporário para mostrar que está processando
        status_texto = st.empty()
        status_texto.markdown("ALDO está pensando...")

       # Envia todo o histórico para a IA ter o contexto da conversa
        resposta_ia = cliente_ia.chat.completions.create(
            # <-- Nome genérico, o LM Studio usa o que estiver na RAM
            model="modelo-local-lmstudio",
            messages=st.session_state.historico_chat,
            temperature=0.3
        )

        texto_final = resposta_ia.choices[0].message.content

        # Substitui a mensagem de "pensando" pelo texto real
        status_texto.markdown(texto_final)

    # 3. Salva a resposta da IA no histórico
    st.session_state.historico_chat.append(
        {"role": "assistant", "content": texto_final})
