# 📈 ALDO - Assistente Financeiro Inteligente

O **ALDO** é um assistente virtual focado em educação financeira, projetado para explicar indicadores econômicos oficiais do Brasil (como Selic, IPCA, CDI, entre outros) de forma didática, acessível e segura.

Este projeto foi construído com foco em **privacidade e precisão**, utilizando uma arquitetura que consome dados reais e orquestra a Inteligência Artificial 100% localmente.

## 🚀 Diferenciais da Arquitetura

* **Zero Alucinação de Dados:** O modelo não utiliza sua memória pré-treinada para informar taxas. Os dados são extraídos em tempo real da API oficial do Banco Central do Brasil via script em Python.
* **Inferência Local (Offline):** O processamento de linguagem natural (LLM) ocorre inteiramente na máquina do usuário via LM Studio, garantindo total privacidade e eliminando custos com APIs de terceiros.
* **Guardrails Rígidos:** O assistente possui instruções estritas para não recomendar investimentos e bloquear perguntas fora do escopo econômico.
* **Interface Web Reativa:** Front-end construído com Streamlit, oferecendo uma experiência de chat fluida com retenção de histórico.

## 🛠️ Tecnologias Utilizadas

* **Python 3:** Motor principal da aplicação.
* **Streamlit:** Construção da interface gráfica (Web UI).
* **LM Studio:** Servidor local de inferência de IA.
* **Modelos Open-Source (GGUF):** Testado e otimizado para rodar com modelos como Llama 3.1 8B Instruct.
* **Requests (API REST):** Integração com o Banco Central do Brasil (SGS - Sistema Gerenciador de Séries Temporais).

## 📁 Estrutura do Repositório

* **`/src`**: Contém o código-fonte da aplicação[cite: 1].
  * `aldo_app.py`: Versão de testes para execução via terminal[cite: 1].
  * `aldo_web.py`: Versão principal com interface gráfica via Streamlit[cite: 1].
  * `requirements.txt`: Lista de dependências do projeto[cite: 1].
* **`/docs`**: Documentação de apoio do projeto[cite: 1].
  * `01-documentacao-agente.md`: Visão geral do comportamento da IA[cite: 1].
  * `03-prompts.md`: Estrutura de injeção de contexto e regras[cite: 1].
  * `04-metricas.md`: Resultados de testes de estresse (QA)[cite: 1].
  * `05-pitch.md`: Roteiro de apresentação da solução[cite: 1].

## ⚙️ Como Executar o Projeto

**1. Preparando o Servidor de IA (LM Studio)**
1. Faça o download e instale o [LM Studio](https://lmstudio.ai/).
2. Baixe um modelo no formato GGUF (recomendação: `Llama-3.1-8B-Instruct-GGUF`).
3. Inicie o "Local Server" no LM Studio na porta `1234`.

**2. Preparando o Ambiente Python**
Clone este repositório e instale as dependências:
```bash
git clone <URL_DO_SEU_REPOSITORIO>
cd src
pip install -r requirements.txt
````

**3. Iniciando o ALDO**
Com o servidor do LM Studio rodando em segundo plano, execute a interface web:
```bash
streamlit run aldo_web.py
```

O navegador abrirá automaticamente em http://localhost:8501 com o assistente pronto para uso!

